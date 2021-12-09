# imports
import typing

from django import forms
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from .models import (
    Theme,
    Settings,
)

User = get_user_model()

if typing.TYPE_CHECKING:
    from django.http import HttpRequest

# End: imports -----------------------------------------------------------------


class SignUpForm(UserCreationForm):

    required_css_class = 'required font-bold'
    code = forms.CharField(required=False, label='Kode')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'gender',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['password1'].help_text = "Your password can't be too similar to your other personal information. \
        Your password must contain at least 8 characters. \
        Your password can't be a commonly used password nor entierly numeric."


class EditUserForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'gender',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    """ AuthenticationForm compatible with Bootstrap. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CustomPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        exclude = []
        labels = {
            'old_password': 'Gammelt passord',
            'new_password1': 'Nytt passord',
            'new_password2': 'Nytt passord bekreftelse',
        }

    def __init__(self, *args, **kwargs):
        request: HttpRequest = kwargs.pop('request')
        super().__init__(request.user, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class SettingsForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = Settings
        exclude = ['user']  # pylint: disable=modelform-uses-exclude

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # retrieve all public themes & user owned themes
        themes = Theme.objects.filter(Q(user=None) | Q(user=user))

        self.fields['account_theme'].queryset = themes
        self.fields['video_theme'].queryset = themes
        self.fields['course_theme'].queryset = themes
        self.fields['song_theme'].queryset = themes
        self.fields['wiki_theme'].queryset = themes
        self.fields['event_theme'].queryset = themes
        self.fields['main_theme'].queryset = themes
        self.fields['input_theme'].queryset = themes
        self.fields['footer_theme'].queryset = themes


class ThemeForm(forms.ModelForm):

    required_css_class = 'required font-bold'

    class Meta:
        model = Theme
        fields = [
            'name',
            'background_color',
            'text_color',
            'link_color',
            'link_hover_color',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
