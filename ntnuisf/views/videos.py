# imports
from django.http import HttpRequest
from django.views import View
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from ..forms.videos import VideoForm, VideoFilterForm
from ..models.videos import Video
# End: imports -----------------------------------------------------------------

# Functions:


def video_search_filter(form, queryset):
    search: str = form.cleaned_data['search']
    tag = form.cleaned_data['tag']
    difficulty = form.cleaned_data['difficulty']

    if search != '':
        queryset = queryset.filter(Q(navn__icontains=search) | Q(beskrivelse__icontains=search) | Q(fokuspunkt__icontains=search))
    if tag != '-1':
        queryset = queryset.filter(tags__id=tag)
    if difficulty != '-1':
        queryset = queryset.filter(difficulty=difficulty)

    return queryset


# End: Functions ---------------------------------------------------------------


@method_decorator([login_required, permission_required('videos.create_video', login_url='forbidden')], name='dispatch')
class AddVideo(View):
    template = 'ntnuisf/videos/video_form.html'
    form_class = VideoForm

    def get(self, request: HttpRequest):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            video = form.save()
            video.embed()
            return redirect('videos:all_videos')

        return render(request, self.template, {'form': form})


edit_video_dec = [login_required, permission_required('videos.change_video', login_url='forbidden')]


@method_decorator(edit_video_dec, name='dispatch')
class EditVideo(View):
    template = 'ntnuisf/videos/video_form.html'
    form_class = VideoForm

    def get(self, request: HttpRequest, video_id: int):
        video = Video.objects.get(id=video_id)
        form = self.form_class(instance=video)
        return render(request, self.template, {'form': form})

    def post(self, request: HttpRequest, video_id: int):
        video = Video.objects.get(id=video_id)
        form = self.form_class(data=request.POST, instance=video)

        if form.is_valid():
            video = form.save()
            video.embed()
            return redirect('videos:all_videos')

        return render(request, self.template, {'form': form, 'video_id': video_id})


view_video_dec = [login_required, permission_required('videos.view_video', login_url='forbidden')]


@method_decorator(view_video_dec, name='dispatch')
class AllVideos(View):
    template = 'ntnuisf/videos/all_videos.html'
    form_class = VideoFilterForm

    def get(self, request: HttpRequest):
        form = self.form_class()
        videos = Video.objects.all()

        return render(request, self.template, {
            'form': form,
            'videos': videos,
        })

    def post(self, request: HttpRequest):
        form = self.form_class(data=request.POST)
        videos = Video.objects.all()

        if form.is_valid():
            videos = video_search_filter(form=form, queryset=videos)

        return render(request, self.template, {
            'form': form,
            'videos': videos,
        })


view_video_dec = [login_required, permission_required('videos.view_video', login_url='forbidden')]


@method_decorator(view_video_dec, name='dispatch')
class VideoView(View):
    template = 'ntnuisf/videos/video_view.html'

    def get(self, request: HttpRequest, video_id: int):
        video = Video.objects.get(id=video_id)
        return render(request, self.template, {'video': video})


delete_video_dec = [login_required, permission_required('videos.delete_video', login_url='forbidden')]


@method_decorator(delete_video_dec, name='dispatch')
class DeleteVideo(View):

    def post(self, request: HttpRequest, video_id: int):
        Video.objects.get(id=video_id).delete()
        return redirect('videos:all_videos')
