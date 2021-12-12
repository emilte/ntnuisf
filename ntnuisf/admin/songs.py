# imports:
from django.http import HttpRequest
from django.contrib import admin

from ..models.songs import Song, Tag

# End: imports -----------------------------------------------------------------


# filters:
class BPMFilter(admin.SimpleListFilter):
    title = 'bpm'
    parameter_name = 'bpm'

    def lookups(self, request: HttpRequest, model_admin):
        return [('slow', 'Less than 62'), ('medium', '63 to 75'), ('fast', 'Greater than 76')]

    def queryset(self, request: HttpRequest, queryset):
        if self.value() is None:
            return queryset

        if self.value() == 'slow':
            return queryset.filter(bpm__lte=62)

        if self.value() == 'medium':
            return queryset.filter(bpm__gte=63, bpm__lte=75)

        if self.value() == 'fast':
            return queryset.filter(bpm__gte=76)

        return queryset


# End: filters -----------------------------------------------------------------


# managers:
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'bpm']
    list_filter = [BPMFilter, 'tags']
    search_fields = ['title', 'artist']
    ordering = ['bpm', 'title']
    readonly_fields = ['created', 'creator']
    filter_horizontal = ['tags']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']
    search_fields = ['title', 'context']
    ordering = ['title']
    readonly_fields = ['created', 'creator']


# End: managers ----------------------------------------------------------------

# admin.site.register(File)
