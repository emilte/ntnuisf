# imports
from django.http import HttpRequest
from django.contrib import admin
from django.db.models import QuerySet
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Permission

from root import models as root_models

from .models import (
    Theme,
    Settings,
    Department,
    Instructor,
    SpotifyToken,
    PermissionCode,
    DepartmentMembership,
)

User = get_user_model()
# End: imports -----------------------------------------------------------------

# pylint: disable=unused-argument


# Actions for Admin-site:
@admin.action(description='Mark selected users as normal users without any permissions')
def make_normal_user(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_staff=False)
    queryset.update(is_superuser=False)


@admin.action(description='Mark selected users as is_staff')
def make_staff_user(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=False)


@admin.action(description='Mark selected users as is_superuser')
def make_superuser(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_staff=True)
    queryset.update(is_superuser=True)


# End: Actions for Admin-site ---------------------------------------------------


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ['username', 'id', 'email', 'first_name', 'last_name', 'gender', 'phone_number', 'spotify_username', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'gender']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'id', 'phone_number']
    ordering = ['last_name']
    readonly_fields = ['last_login', 'date_joined']
    filter_horizontal = ['groups', 'user_permissions']
    actions = [make_normal_user, make_staff_user, make_superuser]


@admin.register(PermissionCode)
class PermissionCodeAdmin(root_models.CustomBaseAdmin):
    list_display = ['group', 'secret']
    list_filter = ['group']
    search_fields = ['group', 'secret']
    ordering = ['-id']
    readonly_fields = []
    # filter_horizontal = []
    # actions = []


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'member_count']
    list_filter = ['parent']
    search_fields = ['name']
    # ordering = []
    # readonly_fields = []
    # filter_horizontal = []
    # actions = []


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['user', 'type']
    list_filter = ['type']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']  # Test


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'background_color', 'text_color', 'link_color', 'link_hover_color']
    list_editable = ['background_color', 'text_color', 'link_color', 'link_hover_color']
    search_fields = ['name', 'creator__email', 'creator__first_name', 'creator__last_name']
    readonly_fields = ['created']


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_theme', 'song_theme', 'course_theme', 'wiki_theme', 'video_theme']
    list_editable = ['account_theme', 'song_theme', 'course_theme', 'wiki_theme', 'video_theme']
    readonly_fields = ['user']
    search_fields = [
        'user__email', 'user__first_name', 'user__last_name', 'account_theme__name', 'song_theme__name', 'course_theme__name', 'video_theme__name',
        'wiki_theme__name'
    ]


# admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(SpotifyToken)
admin.site.register(DepartmentMembership)
