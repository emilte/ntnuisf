# imports
from django.contrib.sites import models as site_models
from django.core.management.base import BaseCommand
# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def show_sites(self):  # pylint: disable=no-self-use
        print('Showing existing sites')
        for s in site_models.Site.objects.all():
            print(f'{s.domain} with id: {s.id}')

    def handle(self, *args, **options):
        self.show_sites()
        # End of handle
