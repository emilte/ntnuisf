# imports
from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from django.contrib.sites import models as site_models
from allauth.socialaccount import models as socialaccount_models

# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def localhost(self):  # pylint: disable=no-self-use
        domain = 'localhost:8000'
        site, created = site_models.Site.objects.get_or_create(name=domain, domain=domain)
        print(f'site created: {created}')
        print(f'Site: {site.domain} ({site.id})')

        try:
            socialapp, created = socialaccount_models.SocialApp.objects.get_or_create(
                provider='google',
                name='Google',
                client_id=settings.GOOGLE_CLIENT_ID,
                secret=settings.GOOGLE_CLIENT_SECRET,
            )
            print(f'socialapp created: {created}')
            socialapp.sites.add(site)
            socialapp.save()

            settings.SITE_ID = site.id

        except Exception as e:  # pylint: disable=broad-except
            print(e)

    def handle(self, *args, **options):
        self.localhost()
        management.call_command('show_sites')
        # End of handle
