# imports
from django.core.management.base import BaseCommand
# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def f(self):
        from django.conf import settings
        print(settings.SITE_ID)

    def handle(self, *args, **options):
        # management.call_command('show_sites')
        self.f()

        # End of handle
