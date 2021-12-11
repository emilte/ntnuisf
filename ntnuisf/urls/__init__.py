from django.urls import include, path

from ..views import songs as song_views

app_name = 'ntnuisf'

urlpatterns = [
    path('', song_views.HomeView.as_view(), name='home'),
    path('forbidden/', song_views.ForbiddenView.as_view(), name='forbidden'),
    path('songs/', include('ntnuisf.urls.songs')),
    path('account/', include('accounts.urls')),
    path('courses/', include('ntnuisf.urls.courses')),
    path('videos/', include('ntnuisf.urls.videos')),
    path('info/', include('ntnuisf.urls.info')),
    path('wiki/', include('ntnuisf.urls.wiki')),
    path('events/', include('ntnuisf.urls.events')),
]
