# imports
import json

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin

# End: imports -----------------------------------------------------------------


# class User(auth_models.User):
class User(AbstractUser, PermissionsMixin):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    # department = models.ForeignKey('accounts.Department', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Avdeling', related_name='users')
    # nickname = models.CharField(max_length=150, unique=True, null=True, blank=False, verbose_name='Kallenavn')
    gender = models.CharField(max_length=1, choices=Gender.choices, default=None, null=True, blank=True, verbose_name='Kjønn')
    phone_number = models.CharField(max_length=13, default=None, null=True, blank=True, verbose_name='Mobilnummer')
    spotify_username = models.CharField(max_length=150, null=True, blank=True)  # Obsolete

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'{self.get_full_name() or self.username or self.email or self.id}'


class PermissionCode(models.Model):
    """ Secret code that users can submit to join groups. """
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    secret = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f'PermissionCode ({self.group}:{self.secret})'


class Department(models.Model):
    """
    Like Group, but with no permissions.

    Can be used for visual affiliations.
    Supports hierarchical departments.
    """
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Navn')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name='Over-seksjon')
    members = models.ManyToManyField(User, through='DepartmentMembership', related_name='departments', verbose_name='Medlemmer')

    class Meta:
        ordering = []
        verbose_name = 'Seksjon'
        verbose_name_plural = 'Seksjoner'

    def __str__(self):
        return f'{self.name}'

    def root_path(self, path=None):
        path = path or []
        path.append(self)
        if self.parent:
            return self.parent.root_path(path)
        return path

    def member_count(self):
        """ Useful in ModelAdmin. """
        return self.members.all().count()


# pylint: disable=consider-using-f-string
class DepartmentMembership(models.Model):
    """ Intermediate model: User <-> Department """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Bruker')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Seksjon')
    date_joined = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name='Dato innmeldt')

    class Meta:
        ordering = ['id']
        verbose_name = 'Medlem'
        verbose_name_plural = 'Medlemmer'

    def __str__(self):
        return f'Medlem: {self.user}'


class Theme(models.Model):
    creator = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='themes',
        verbose_name='Eier',
        help_text='Dersom eier er satt, vil temaet være privat'
    )
    name = models.CharField(max_length=140, null=True, blank=False, verbose_name='Navn')

    css_help_text = 'CSS eg: blue, rgba(0,0,255, 0.5)'
    background_color = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Bakgrunnsfarge', help_text=css_help_text)
    text_color = models.CharField(max_length=140, null=True, verbose_name='Tekstfarge', help_text=css_help_text)
    link_color = models.CharField(max_length=140, null=True, verbose_name='Linkfarge', help_text=css_help_text)
    link_hover_color = models.CharField(max_length=140, null=True, verbose_name='Link hover farge', help_text=css_help_text)

    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')

    class Meta:
        ordering = ['creator', 'name']
        verbose_name = 'Tema'
        verbose_name_plural = 'Temaer'

    def __str__(self):
        if self.creator:
            return f'{self.name}'
        return f'{self.name} (Public)'

    def as_css(self):
        css = """.user-theme {{
            background-color: {0};
            color: {1};
        }}
        .user-theme a {{
            color: {2};
        }}
        .user-theme a:hover {{
            color: {3};
        }}
        """.format(self.background_color or 'sd', self.text_color, self.link_color, self.link_hover_color)
        return css

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='settings', verbose_name='Tilhører')

    account_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_account', verbose_name='Bruker-tema')
    video_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_video', verbose_name='Turbibliotek-tema')
    event_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_event', verbose_name='Event-tema')
    course_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_course', verbose_name='Kurs-tema')
    song_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_song', verbose_name='Musikk-tema')
    wiki_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_wiki', verbose_name='Wiki-tema')

    # Advanced
    background = models.CharField(max_length=1000, default=None, null=True, blank=True, verbose_name='Bakgrunn URL', help_text='Bildeaddresse')
    scrollbar = models.CharField(max_length=1000, default=None, null=True, blank=True, verbose_name='Scrollbar farge')
    main_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_main', verbose_name='Hoved-tema')
    input_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_input', verbose_name='Input-tema')
    footer_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='settings_as_footer', verbose_name='Footer-tema')

    class Meta:
        verbose_name = 'Instilling'
        verbose_name_plural = 'Instillinger'

    def __str__(self):
        return 'Instillinger for {}'.format(self.user)


class Instructor(models.Model):
    TYPES = [
        (0, '------'),
        (1, 'lead'),
        (2, 'follow'),
        (3, 'hjelpeinstruktør'),
        (4, 'annet'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='instructor_set')
    type = models.IntegerField(choices=TYPES, default=0)

    class Meta:
        ordering = ['type']
        verbose_name = 'Instruktør'
        verbose_name_plural = 'Instruktører'

    def __str__(self):
        return f'{self.user} ({self.get_type_display()})'


class SpotifyToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='spotify_token')
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Spotify token for {self.user}'

    def add_info(self, data):
        self.info = json.dumps(data)
        self.save()
