# imports
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# End: imports -----------------------------------------------------------------


class Tag(models.Model):

    title = models.CharField(null=True, blank=False, max_length=100, unique=True, verbose_name='Tittel')
    context = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text='Mellomrom-separerte nøkkelord for å relatere tag til kategori (Blank for ikke spesifikk type). Bruk: song, course eller video.'
    )

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, verbose_name='Opprettet av')
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')

    def __str__(self):
        return self.title

    def context_list(self) -> list[str]:
        if self.context:
            return self.context.split(' ')
        return []

    @staticmethod
    def get_queryset(context_list=None):
        a = Tag.objects.all()
        if not context_list:
            return a

        q = a.filter(context=None)
        for c in context_list:
            q = q | a.filter(context__icontains=c)
        return q

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)


class Song(models.Model):
    title = models.CharField(max_length=150, null=True, blank=False, verbose_name='Tittel')
    artist = models.CharField(max_length=150, null=True, blank=False)
    bpm = models.SmallIntegerField(blank=True, null=True, help_text='Helst antall partall per minutt')
    spotify_URL = models.URLField(null=True, blank=False, help_text='Høyre klikk på sang -> Share -> Copy Song Link')
    spotify_URI = models.CharField(max_length=300, null=True, blank=False, help_text='Høyre klikk på sang -> Share -> Copy Spotify URI')
    tags = models.ManyToManyField(Tag, blank=True)

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, verbose_name='Opprettet av')
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')

    class Meta:
        ordering = ['bpm', 'title']
        verbose_name = 'Sang'
        verbose_name_plural = 'Sanger'

    def __str__(self):
        return f'{self.title} - {self.artist} ({self.bpm} bpm)'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)


class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='mediaroot/')

    def __str__(self):
        return f'File {self.id}'
