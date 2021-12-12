# imports
from halo import Halo

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()
# End: imports -----------------------------------------------------------------

# Settings:
USER_PW = 'Django123'


class Command(BaseCommand):

    def createsu(self):  # pylint: disable=no-self-use
        spinner = Halo('Creating superuser')
        spinner.start()
        email = 'admin@admin.com'
        User.objects.create_superuser(email=email, password=USER_PW, first_name='Admin', last_name='Adminsen', phone_number='12345678')
        spinner.succeed('Creating superuser. email: {email}, password: {USER_PW}')

    def handle(self, *args, **options):
        try:
            self.createsu()
        except Exception as e:  # pylint: disable=broad-except
            print(e)
        # End of handle
