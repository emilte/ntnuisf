# imports
from django.core import management
from django.core.management.base import BaseCommand
# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            management.call_command('create_admin')
            management.call_command('site_heroku')
            management.call_command('SITE_ID')
            # management.call_command('flush', interactive=False)
            management.call_command('myseed')
        except Exception as e:
            print(e)

        # End of handle
