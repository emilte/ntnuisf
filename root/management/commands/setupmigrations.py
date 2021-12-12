# imports
import os
from django.conf import settings
from django.core.management.base import BaseCommand

# End: imports -----------------------------------------------------------------


# pylint: disable=all
class Command(BaseCommand):

    def handle(self, *args, **options):
        for app in settings.PROJECT_APPS:

            try:
                path = app.replace('.', '/')
                migrations = f'{path}/migrations'
                os.mkdir(migrations)
                init = f'{migrations}/__init__.py'
                open(init, 'a', encoding='utf-8').close()

            except Exception as e:  # pylint: disable=broad-except
                # print(f'{app} failed. {e}')
                pass
