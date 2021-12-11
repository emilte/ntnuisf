# imports
from django.urls import path

from ..views import videos as video_views
# End: imports -----------------------------------------------------------------

app_name = 'videos'

urlpatterns = [
    path('add/', video_views.AddVideo.as_view(), name='add_video'),
    path('all/', video_views.AllVideos.as_view(), name='all_videos'),
    path('<int:video_id>', video_views.VideoView.as_view(), name='video_view'),
    path('edit/<int:video_id>', video_views.EditVideo.as_view(), name='edit_video'),
    path('delete/<int:video_id>', video_views.DeleteVideo.as_view(), name='delete_video'),
]
