# imports
import shutil
import typing

from django.conf import settings
from django.core.management.base import BaseCommand

if typing.TYPE_CHECKING:
    from pathlib import PosixPath

# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            dest='appname',
            help='appname <appname>',
        )

    def handle(self, *args, **options):
        appname: str = options['appname']
        workspace: PosixPath = settings.BASE_DIR.parent
        print(1, workspace)

        skeleton_name = 'app_skeleton'
        app_skeleton: PosixPath = settings.BASE_DIR / 'management/commands' / skeleton_name
        print(2, app_skeleton)
        new_app: PosixPath = workspace / 'sdfsdfs'
        print(3, new_app)
        shutil.copytree(str(app_skeleton), str(workspace))
