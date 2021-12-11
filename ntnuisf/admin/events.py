from django.contrib import admin
from ..models.events import Event, Participant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'place']
    ordering = ['start', 'title']
    list_filter = []
    readonly_fields = ['creator', 'created', 'last_edited', 'last_editor']
    filter_horizontal = ['participants']
    search_fields = ['title', 'place']

    # search_fields = ['instructors'] # test
    # autocomplete_fields = ['instructors'] # test


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'date_joined', 'is_earlybird']
    ordering = ['event__start']
    list_filter = ['is_earlybird']
    readonly_fields = ['date_joined']
    filter_horizontal = []
    search_fields = ['user', 'event']
