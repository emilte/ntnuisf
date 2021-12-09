# imports
from django import forms
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth import models as auth_models

# End: imports -----------------------------------------------------------------

# https://github.com/django/django/blob/master/django/forms/models.py


class CustomModelForm(forms.ModelForm):

    def save(self, *args, commit=True, **kwargs):  # pylint: disable=arguments-differ
        """
        Override django ModelForm.save() to implement kwargs. Do not use super() in this class!
        Changes: user arg is added

        Source __doc__:
        Save this form's self.instance object if commit=True. Otherwise, add
        a save_m2m() method to the form which can be called after the instance
        is saved manually at a later time. Return the model instance.
        """
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate." % ( # pylint: disable=consider-using-f-string
                    self.instance._meta.object_name,
                    'created' if self.instance._state.adding else 'changed',  # pylint: disable=protected-access
                )
            )  # pylint: disable=consider-using-f-string
        if commit:
            # If committing, save the instance and the m2m data immediately.
            self.instance.save(*args, **kwargs)  # <--- This is the only difference
            self._save_m2m()
        else:
            # If not committing, add a method to the form to allow deferred
            # saving of m2m data.
            self.save_m2m = self._save_m2m  # pylint: disable=attribute-defined-outside-init
        return self.instance


class CustomBaseAdmin(admin.ModelAdmin):
    readonly_fields = ['creator', 'created', 'last_edited', 'last_editor']

    # list_display = []
    # ordering = []
    # list_filter = []
    # filter_horizontal = []
    # search_fields = []

    def save_model(self, request, obj, form, change):
        try:
            if not change:
                obj.creator = request.user
                obj.created = timezone.now()
            obj.last_editor = request.user
            obj.last_edited = timezone.now()
        except Exception as _:  # pylint: disable=broad-except
            pass

        return super().save_model(request, obj, form, change)


class CustomBaseModel(models.Model):
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name='editor_%(class)s_set',
        verbose_name='Sist redigert av'
    )
    last_edited = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Sist redigert')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name='creator_%(class)s_set',
        verbose_name='Opprettet av'
    )
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')

    class Meta:
        abstract = True

    def is_edited(self):
        return self.created != self.last_edited

    def clean(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.clean()
        user = kwargs.pop('user', None)  # Must pop because super().save() doesn't accept user
        if isinstance(user, auth_models.AnonymousUser):
            user = None  # creator and last_editor can't be AnonymousUser
        if not self.id:
            self.created = timezone.now()
            if user:
                self.creator = user
        self.last_edited = timezone.now()
        if user:
            self.last_editor = user

        super().save(*args, **kwargs)
