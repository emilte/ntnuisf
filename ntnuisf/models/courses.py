# imports
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from accounts.models import Instructor

from ..models.videos import Video
from ..models.songs import Song, Tag

User = get_user_model()
# End: imports -----------------------------------------------------------------

semesters = ['------']
v = [f'V{year}' for year in range(2000, 2100)]
h = [f'H{year}' for year in range(2000, 2100)]
semesters.extend(v)
semesters.extend(h)
SEMESTER_CHOICES = [(i, semesters[i]) for i in range(len(semesters))]


class Course(models.Model):
    title = models.CharField(max_length=140, null=True, blank=False, verbose_name='Tittel')
    place = models.CharField(max_length=140, null=True, blank=True, verbose_name='Sted')
    date = models.DateField(null=True, blank=True, verbose_name='Dato')
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True, verbose_name='Slutt')
    lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_courses', verbose_name='Instruktør (lead)')
    follow = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='follow_courses', verbose_name='Instruktør (follow)')
    comments = models.TextField(null=True, blank=True, verbose_name='Kommentarer')
    tags = models.ManyToManyField(Tag, blank=True)
    semester_char = models.CharField(max_length=5, null=True, blank=True)
    external = models.BooleanField(default=False, verbose_name='Eksternkurs')
    bulk = models.PositiveIntegerField(null=True, blank=True, verbose_name='Bolk')
    day = models.PositiveIntegerField(null=True, blank=True, verbose_name='Dag')

    last_edited = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Sist redigert')
    last_editor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name='last_edited_courses', verbose_name='Sist redigert av'
    )
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name='Opprettet')
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, editable=False, related_name='created_courses', verbose_name='Opprettet av'
    )

    # NOTE: Under development
    # instructors = models.ManyToManyField(User)
    instructors = models.ManyToManyField(Instructor, blank=True)
    semester_choice = models.IntegerField(choices=SEMESTER_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ['date', 'bulk', 'day', 'title']
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurs'

    def __str__(self):
        if self.external:
            return f'{self.semester_char} {self.title}'
        return f'{self.semester_char}, Bolk {self.bulk}, Dag {self.day}'

    def get_absolute_url(self):
        return reverse('view_course', kwargs={'course_id': self.pk})

    def get_semester(self):
        _semesters = ['Vår', 'Høst']
        if self.date:
            i = (self.date.month - 1) // 6  # Calculates first (0) or second (1) half of year
            return f'{_semesters[i]} {self.date.year}'
        return None

    def get_date(self):
        try:
            return self.date.strftime('%d.%m.%y')
        except:  # pylint: disable=bare-except
            return None

    def get_start(self):
        try:
            return self.start.strftime('%H:%M')
        except:  # pylint: disable=bare-except
            return None

    def get_end(self):
        try:  # pylint: disable=bare-except
            return self.end.strftime('%H:%M')
        except:  # pylint: disable=bare-except
            return None

    def get_tags(self):
        return [title[0] for title in self.tags.all().values_list('title')]

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_edited = timezone.now()

        if self.date:
            _semesters = ['V', 'H']
            i = (self.date.month - 1) // 6  # Calculates first (0) or second (1) half of year
            self.semester_char = f'{_semesters[i]}{self.date.year}'

        return super().save(*args, **kwargs)


class CourseSection(models.Model):
    title = models.CharField(max_length=140, null=True, blank=False, verbose_name='Tittel')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='sections', verbose_name='Kurs')
    description = models.TextField(null=True, blank=True, verbose_name='Beskrivelse')
    start = models.TimeField(null=True, blank=True)
    # duration = models.FloatField(null=True, blank=False, verbose_name='Varighet')
    duration = models.FloatField(default=7.5, null=True, blank=False, verbose_name='Varighet')
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True, related_name='sections', verbose_name='Sang')
    song2 = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True, related_name='sections_song2', verbose_name='Sang')
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True, blank=True, related_name='sections', verbose_name='Video')
    nr = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['nr']
        verbose_name = 'Kurs-seksjon'
        verbose_name_plural = 'Kurs-seksjoner'

    def __str__(self):
        return f'Section ({self.nr}) in course: {self.course}'

    def get_course(self):
        return self.course or None

    def get_start(self):
        return self.start.strftime('%H:%M')

    def get_song(self):
        return self.song or None
