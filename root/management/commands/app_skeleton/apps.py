from django.apps import AppConfig


class AppSkeletonConfig(AppConfig):
    name = 'app_skeleton'

    def ready(self):
        from . import signals  # pylint: disable=unused-import import-outside-toplevel
