# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from halo import Halo
from django.core import management
from accounts.models import *
from ntnuisf.models.songs import *
# End: imports -----------------------------------------------------------------

# Settings:

# pylint: disable=all


class Command(BaseCommand):

    def create_themes(self):
        spinner = Halo('Creating themes')
        spinner.start()
        Theme.objects.create(
            background_color='red',
            link_color='blue',
            link_hover_color='yellow',
        )
        spinner.succeed()

    def handle(self, *args, **options):
        self.create_themes()
        # End of handle
