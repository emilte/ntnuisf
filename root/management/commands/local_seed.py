# imports
from django.core import management
from django.core.management.base import BaseCommand
# End: imports -----------------------------------------------------------------

# OBS: seed() on instance was depricated for Faker module.
# Manually edited django-seed module __init__.py on line 35 from seed to seed_instance


class Command(BaseCommand):

    def handle(self, *args, **options):
        # management.call_command('flush', interactive=False)
        management.call_command('create_admin')
        management.call_command('site_localhost')

        try:
            management.call_command('myseed')
        except Exception as e:  # pylint: disable=broad-except
            print(e)
        # End of handle
