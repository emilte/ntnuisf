# imports:
from django.contrib import admin

from ..models.videos import Video
# End: imports -----------------------------------------------------------------


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty']
    list_editable = ['difficulty']
    list_filter = ['tags', 'difficulty']
    search_fields = ['title', 'creator__email', 'creator__first_name', 'creator__last_name']
    ordering = ['difficulty', 'title']
    readonly_fields = ['created', 'creator']
    filter_horizontal = ['tags']
