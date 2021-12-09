from django.apps import AppConfig
from django.core import management
from django.core.management.base import CommandError


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from . import signals  # pylint: disable=unused-import import-outside-toplevel

        try:
            # define credentials in '.env' file
            management.call_command('createsuperuser', interactive=False)
        except CommandError as e:
            # multiple calls of 'createsuperuser' will raise exception because the username is already taken
            print(__file__, e)
