# imports
import typing

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import Group

from root import models as root_models

User = get_user_model()

if typing.TYPE_CHECKING:
    pass
# End: imports -----------------------------------------------------------------


class SomeMixin():
    """ Get something """

    def get_some(self, thing: dict[str, int]) -> int:
        print(f'Getting something as {str(self)}')
        return thing.get('some')


class Example(SomeMixin, root_models.CustomBaseModel):

    class Kind(models.TextChoices):
        SOME = 'S', 'Some'
        THING = 'T', 'Thing'

    kind = models.CharField(max_length=1, choices=Kind.choices, default=None, null=True, blank=True, verbose_name='kind')
    some = models.CharField(max_length=13, default=None, null=True, blank=True, verbose_name='Some')
    thing = models.CharField(max_length=13, default=None, null=True, blank=True, verbose_name='Thing')
    groups = models.ManyToManyField(to=Group, through='GroupMembership')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, related_name='examples')

    class Meta:
        ordering = ['some', 'thing']
        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        return f'Example: {self.id}'


class GroupMembership(models.Model):
    """ Intermediate model: Example <-> Group """
    example = models.ForeignKey(Example, on_delete=models.CASCADE, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    date_joined = models.DateTimeField(default=timezone.now, null=False, blank=False)

    class Meta:
        ordering = ['date_joined']

    def __str__(self):
        return f'Membership: {self.user} {str(self.group)}'
