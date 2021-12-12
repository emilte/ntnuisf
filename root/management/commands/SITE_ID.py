# imports
from django.conf import settings
from django.core.management.base import BaseCommand

# End: imports -----------------------------------------------------------------


# pylint: disable=all
class Command(BaseCommand):

    def f(self):  # pylint: disable=no-self-use
        print(settings.SITE_ID)

    def handle(self, *args, **options):
        # management.call_command('show_sites')
        self.f()

        # End of handle
