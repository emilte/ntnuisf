# imports
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from ntnuisf.models.songs import Tag

User = get_user_model()
# End: imports -----------------------------------------------------------------

# choises:
DIFFICULY_CHOISES = [
    (1, 'Lett'),
    (2, 'Middels'),
    (3, 'Vanskelig'),
]
# End: coises ------------------------------------------------------------------


class Video(models.Model):
    title = models.CharField(max_length=150, null=True, blank=False, verbose_name='Tittel')
    youtube_URL = models.URLField(null=True, blank=False)
    embedded = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(null=True, blank=True, verbose_name='Beskrivelse')
    focus = models.TextField(null=True, blank=True, verbose_name='Fokuspunkt')
    difficulty = models.IntegerField(choices=DIFFICULY_CHOISES, default=1, verbose_name='Vanskelighetsgrad')

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, verbose_name='Opprettet av')
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')

    class Meta:
        ordering = ['id']
        verbose_name = 'Video'
        verbose_name_plural = 'Videoer'

    def embed(self):
        video_id = 'no id'
        if self.youtube_URL is None:
            return

        if 'youtu.be' in self.youtube_URL:
            video_id = self.youtube_URL.split('/')[-1].split('?')[0]  # pylint: disable=use-maxsplit-arg,fixme # TODO: what is this?

        if 'watch' in self.youtube_URL:
            video_id = self.youtube_URL.split('?')[1].split('&')[0][2:]

        self.embedded = 'https://www.youtube.com/embed/' + video_id + '?iv_load_policy=3' + '?rel=0'
        self.save()

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
