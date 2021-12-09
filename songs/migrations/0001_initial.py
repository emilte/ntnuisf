# Generated by Django 2.2.9 on 2020-02-01 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='mediaroot/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, unique=True, verbose_name='Tittel')),
                ('context', models.CharField(blank=True, help_text='Mellomrom-separerte nøkkelord for å relatere tag til kategori (Blank for ikke spesifikk type). Bruk: song, course eller video.', max_length=100, null=True)),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Tittel')),
                ('artist', models.CharField(max_length=150, null=True)),
                ('bpm', models.SmallIntegerField(blank=True, help_text='Helst antall partall per minutt', null=True)),
                ('spotify_URL', models.URLField(help_text='Høyre klikk på sang -> Share -> Copy Song Link', null=True)),
                ('spotify_URI', models.CharField(help_text='Høyre klikk på sang -> Share -> Copy Spotify URI', max_length=300, null=True)),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('tags', models.ManyToManyField(blank=True, to='songs.Tag')),
            ],
            options={
                'verbose_name': 'Sang',
                'verbose_name_plural': 'Sanger',
                'ordering': ['bpm', 'title'],
            },
        ),
    ]
