from django.urls import include, path

from .. import views as ntnuisf_views

app_name = 'ntnuisf'

urlpatterns = [
    path('', ntnuisf_views.IndexView.as_view(), name='index'),
    path('forbidden/', ntnuisf_views.ForbiddenView.as_view(), name='forbidden'),
    path('courses/', include('ntnuisf.urls.courses')),
    path('events/', include('ntnuisf.urls.events')),
    path('info/', include('ntnuisf.urls.info')),
    path('songs/', include('ntnuisf.urls.songs')),
    path('videos/', include('ntnuisf.urls.videos')),
    path('wiki/', include('ntnuisf.urls.wiki')),
]
