# imports
import typing

from django.core import management
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

if typing.TYPE_CHECKING:
    from django.core.management.base import CommandParser

# End: imports -----------------------------------------------------------------

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            '--noinput',
            '--no-input',
            action='store_false',
            dest='interactive',
            help='Tells Django to NOT prompt the user for input of any kind.',
        )

    def handle(self, *args, **options):
        print('\n== COMMAND: example ==')
        if options['interactive']:
            ...
            # prompt something
            # do something based on input
            # e.g. call other command or abort
            # management.call_command('makemigrations')
        # finally do something

        # End: handle
