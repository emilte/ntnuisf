# imports
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# End: imports -----------------------------------------------------------------


class Event(models.Model):
    title = models.CharField(max_length=140, null=True, blank=False, verbose_name='Tittel')
    place = models.CharField(max_length=140, null=True, blank=True, verbose_name='Sted')
    start = models.DateTimeField(null=True, blank=True, verbose_name='Start')
    end = models.DateTimeField(null=True, blank=True, verbose_name='Slutt')
    description = models.TextField(null=True, blank=True, verbose_name='Beskrivelse')
    facebook_url = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    earlybirds = models.IntegerField(null=True, blank=True)
    earlybird_limit = models.IntegerField(default=100, null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)
    earlybird_price = models.IntegerField(null=True, blank=True)

    participants = models.ManyToManyField(User, through='Participant', blank=True, related_name='events', verbose_name='Påmeldte')

    last_edited = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Sist redigert')
    last_editor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name='edited_eventset', verbose_name='Sist redigert av'
    )
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name='creator_eventset', verbose_name='Opprettet av'
    )

    class Meta:
        ordering = ['-start', 'title']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):

        if not self.id:
            self.created = timezone.now()
        self.last_edited = timezone.now()

        return super().save(*args, **kwargs)


class Participant(models.Model):
    """ Intermediate model: Event -> User """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Bruker')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Event')
    date_joined = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name='Dato påmeldt')
    is_earlybird = models.BooleanField(default=False, verbose_name='Earlybird')
    has_paid = models.BooleanField(default=False, verbose_name='Har betalt')

    class Meta:
        ordering = ['id']
        verbose_name = 'Deltaker'
        verbose_name_plural = 'Deltakere'

    def __str__(self):
        return f'Participant: {self.user}'
