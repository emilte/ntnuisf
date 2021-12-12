# imports
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from ..views import songs
# End: imports -----------------------------------------------------------------

app_name = 'songs'

urlpatterns = [
    path('all/', songs.AllSongsView.as_view(), name='all_songs'),
    path('add/', songs.AddSongView.as_view(), name='add_song'),
    path('edit/<int:song_id>', songs.EditSongView.as_view(), name='edit_song'),
    path('delete/<int:song_id>', songs.DeleteSongView.as_view(), name='delete_song'),
    path('bpm_calc/', songs.BPMView.as_view(), name='bpm_calc'),
    path('tags/add', songs.AddTag.as_view(), name='add_tag'),
    path('tags/edit/<int:tag_id>', songs.EditTag.as_view(), name='edit_tag'),
    path('tags/all', songs.AllTags.as_view(), name='all_tags'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
