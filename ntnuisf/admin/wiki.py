from django.contrib import admin

from ..models.wiki import Folder, Page


@admin.register(Page)
class PageManager(admin.ModelAdmin):
    list_display = ['title', 'folder', 'path', 'private']
    list_editable = ['path', 'private']
    search_fields = ['title', 'folder__title']
    ordering = ['title']
    readonly_fields = ['content', 'last_edited', 'last_editor', 'created', 'creator']

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)


@admin.register(Folder)
class FolderManager(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'creator__email', 'creator__first_name', 'creator__last_name']
    ordering = ['title']
    readonly_fields = ['last_edited', 'last_editor', 'created', 'creator']

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user
        super().save_model(request, obj, form, change)
