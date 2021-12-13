# imports
from __future__ import print_function
import json

from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from ..models.songs import Song, Tag
from ..forms.songs import SongForm, SongSearchForm, TagForm

# End: imports -----------------------------------------------------------------


# Functions
def update_songs_txt(song: Song, title=None):
    tags = song.tags.values_list('navn')
    tags = [t[0] for t in tags]
    song = song.__dict__
    song = {'title': song['title'], 'artist': song['artist'], 'bpm': song['bpm'], 'tags': tags, 'spotify': song['spotify'], 'URI': song['URI']}
    # Add:
    if title is None:
        with open('songs/static/songs/songs.txt', mode='a', encoding='UTF-8') as songs:
            songs.write(json.dumps(song, ensure_ascii=False) + '\n')
    # Update line:
    else:
        with open('songs/static/songs/songs.txt', mode='r', encoding='UTF-8') as songs:
            data = songs.readlines()

        for i, _ in enumerate(data):
            if title in data[i]:
                data[i] = json.dumps(song, ensure_ascii=False) + '\n'

        with open('songs/static/songs/songs.txt', mode='w', encoding='UTF-8') as songs:
            songs.write(''.join(data) + '\n')


# End: Functions ---------------------------------------------------------------



@method_decorator([login_required], name='dispatch')
class AddSongView(View):
    template = 'ntnuisf/songs/song_form.html'
    form_class = SongForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #update_songs_txt(song)
            messages.success(request, 'Du har klart å legge til en ny sang, så flink! :3')
            return redirect('songs:all_songs')
        return render(request, self.template, {'form': form})


@method_decorator([login_required, permission_required('songs.change_song', login_url='forbidden')], name='dispatch')
class EditSongView(View):
    template = 'ntnuisf/songs/song_form.html'
    form_class = SongForm

    def get(self, request, song_id):
        song: Song = Song.objects.get(id=song_id)
        form = self.form_class(instance=song)
        return render(request, self.template, {'form': form})

    def post(self, request, song_id):
        song = Song.objects.get(id=song_id)
        form = self.form_class(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            #update_songs_txt(song)
            return redirect('songs:all_songs')
        return render(request, self.template, {'form': form, 'song_id': song_id})


@method_decorator([login_required], name='dispatch')
class AllSongsView(View):
    template = 'ntnuisf/songs/all_songs.html'
    form_class = SongSearchForm

    def get(self, request):
        form = self.form_class()
        songs = Song.objects.all()
        return render(request, self.template, {'form': form, 'songs': songs.order_by('bpm')})

    def post(self, request):
        form = self.form_class(data=request.POST)
        songs = Song.objects.all()
        if form.is_valid():
            songs = self.search_song_filter(form=form, queryset=songs)
        return render(request, self.template, {'form': form, 'songs': songs.order_by('bpm')})

    def search_song_filter(self, form, queryset):  # pylint: disable=no-self-use
        search = form.cleaned_data['search']
        tag = form.cleaned_data['tag']
        check_min = form.cleaned_data['check_min']
        min_bpm = form.cleaned_data['min_bpm']
        check_max = form.cleaned_data['check_max']
        max_bpm = form.cleaned_data['max_bpm']

        if search != '':
            queryset = queryset.filter(Q(title__icontains=search) | Q(artist__icontains=search))
        if tag != '-1':
            queryset = queryset.filter(tags__id=tag)
        if check_min and min_bpm is not None:
            queryset = queryset.filter(bpm__gte=min_bpm)
        if check_max and max_bpm is not None:
            queryset = queryset.filter(bpm__lte=max_bpm)

        return queryset


@method_decorator([login_required, permission_required('songs.delete_song', login_url='forbidden')], name='dispatch')
class DeleteSongView(View):

    def post(self, request, song_id):
        Song.objects.get(id=song_id).delete()
        messages.success(request, 'Sangen har blitt slettet.')
        return redirect('songs:all_songs')


class BPMView(View):
    # https://github.com/selwin/django-user_agents
    template = 'ntnuisf/songs/bpm_calc.html'

    def get(self, request):
        return render(request, self.template)



class AddTag(View):
    template = 'ntnuisf/songs/tag_form.html'
    form_class = TagForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('songs:all_tags')
        return render(request, self.template, {'form': form})


class EditTag(View):
    template = 'ntnuisf/songs/tag_form.html'
    form_class = TagForm

    def get(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        form = self.form_class(instance=tag)
        return render(request, self.template, {'form': form})

    def post(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        form = self.form_class(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            return redirect('songs:all_tags')
        return render(request, self.template, {'form': form})


class AllTags(View):
    template = 'ntnuisf/songs/all_tags.html'

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, self.template, {'tags': tags})
