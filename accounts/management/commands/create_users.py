# imports
from halo import Halo

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()
# End: imports -----------------------------------------------------------------

# Settings:
USER_PW = 'Django123'


class Command(BaseCommand):

    def createsu(self):
        spinner = Halo('Creating superuser')
        spinner.start()
        email = 'admin@admin.com'
        User.objects.create_superuser(email=email, password=USER_PW, first_name='Admin', last_name='Adminsen', phone_number='12345678')
        spinner.succeed(f'Creating superuser. email: {email}, password: {USER_PW}')

        spinner = Halo('Creating superuser')
        spinner.start()
        email = 'emil.telstad@gmail.com'
        User.objects.create_superuser(
            email=email, password=USER_PW, first_name='Emil', last_name='Telstad', spotify_username='emiltelstad', phone_number='41325358'
        )
        spinner.succeed(f'Creating superuser. email: {email}, password: {USER_PW}')
        # End: createsu

    def create_staff(self):
        spinner = Halo('Creating a staff user')
        spinner.start()
        email = 'staff@staff.com'
        User.objects.create_user(email=email, password=USER_PW, first_name='Staff', last_name='Staffski', is_staff=True, phone_number='87654321')
        spinner.succeed(f'Creating staff user. email: {email}, password: {USER_PW}')

    def create_user(self):
        spinner = Halo('Creating a user')
        spinner.start()
        email = 'user@user.com'
        User.objects.create_user(email=email, password=USER_PW, first_name='User', last_name='Normal', phone_number='87654321')
        spinner.succeed(f'Creating user. email: {email}, password: {USER_PW}')

    def handle(self, *args, **options):
        User.objects.all().delete()
        self.createsu()
        self.create_staff()
        self.create_user()
        # End of handle
