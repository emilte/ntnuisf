# # imports
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# # from accounts import models as # # #from allauth.account import signals as allauth_signals
# #
# from django.contrib.auth import get_user_model

# User = get_user_model()
# #from email.message import EmailMessage

import smtplib

from email.message import EmailMessage
from allauth.account import signals as allauth_signals

from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save

from .models import Settings

User = get_user_model()

# # End: imports -----------------------------------------------------------------

# # @receiver(post_save, sender=User)
# # def permissions(sender, instance, created, **kwargs):
# #     if created:
# #
# #         brukere_models.Account.objects.create(user=instance)
# #         print('== (brukere.signals.py) Account for {} created =='.format(instance))

# # @receiver(allauth_signals.user_signed_up)
# # def create_settings(request, user, **kwargs):
# #     Settings.objects.get_or_create(user=user)
# #     print('== (users.signals.py) <Settings> created for <{}> =='.format(user))
# #
# #
# #
# # @receiver(allauth_signals.user_signed_up)
# # def send_mail(request, user, **kwargs):
# #     try:
# #         server = smtplib.SMTP_SSL('smtp.gmail.com')
# #
# #         sent_from = 'script97tester@gmail.com'
# #         password = 'Django!23'
# #
# #         server.login(sent_from, password)
# #
# #         to = ['emil.telstad@gmail.com']
# #
# #         email = EmailMessage()
# #         email.set_content(f'{instance.email} har opprettet en bruker.')
# #
# #         email['Subject'] = 'Varsel: Ny bruker'
# #         email['From'] = sent_from
# #         email['To'] = to
# #
# #         server.send_message(email)
# #
# #     except Exception as e:
# #         print(e)


@receiver(allauth_signals.user_signed_up)
def create_settings(request, user, **kwargs):
    Settings.objects.get_or_create(user=user)
    print(f'== (users.signals.py) <Settings> created for <{user}> ==')


@receiver(allauth_signals.user_signed_up)
def send_mail(request, user: User, **kwargs):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')

        sent_from = 'script97tester@gmail.com'
        password = 'Django!23'

        server.login(sent_from, password)

        to = ['emil.telstad@gmail.com']

        email = EmailMessage()
        email.set_content(f'{user.email} har opprettet en bruker.')

        email['Subject'] = 'Varsel: Ny bruker'
        email['From'] = sent_from
        email['To'] = to

        server.send_message(email)

    except Exception as e:  # pylint: disable=broad-except
        print(e)
