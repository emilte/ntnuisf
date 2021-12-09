# imports
import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

# End: imports -----------------------------------------------------------------

# yapf: disable
app_structure = [
    {'management': [
        {'commands': [
            '__init__.py',
        ]},
    ]},
    {'migrations': [ # Added from startapp
        '__init__.py',
    ]},
    {'tests': [
        '__init__.py',
        'test_models.py',
        'test_views.py',
        'test_forms.py',
    ]},
    {'templates': [
        {'appname': []},
    ]},
    {'static': [
        {'appname': [
            {'css': ['example.css']},
            {'scss': []},
            {'js': []},
            {'img': []},
        ]},
    ]},
    '__init__.py',
    'admin.py', # Added from startapp
    'apps.py', # Added from startapp
    'forms.py',
    'models.py', # Added from startapp
    'signals.py',
    'tests.py', # Added from startapp
    'urls.py',
    'views.py', # Added from startapp
]
# yapf: enable


def recursive_creation(structure, appname, path):
    """
    Recursively generate folders and files given a structure

    structure: list
        - a description of files (strings) and folders (dictionaries).
        Each folder has another layer of structure.

    appname: string
        - A name to use instead of "appname" in structures

    path: string
        - current working directory
    """

    for item in structure:
        if isinstance(item, dict):
            folder = list(item.keys())[0]
            foldername = appname if folder == "appname" else folder
            newpath = path / foldername
            try:
                os.mkdir(newpath)
            except Exception:
                pass

            recursive_creation(item[folder], appname, newpath)
        else:
            filepath = path / item
            open(filepath, 'a', encoding='utf-8').close()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            dest='appname',
            help='appname <appname>',
        )

    def handle(self, *args, **options):

        appname = options['appname']
        management.call_command("startapp", appname)

        path = settings.BASE_DIR / appname
        recursive_creation(app_structure, appname, path)
