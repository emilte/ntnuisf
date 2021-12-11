# imports
from django.http import HttpRequest
from django.contrib import admin
from django.db.models import QuerySet

from root import models as root_models
from . import models

# End: imports -----------------------------------------------------------------

# pylint: disable=unused-argument...


# Actions:
@admin.action(description='Do something to selected rows')
def example_action(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_active=False)


# End: Actions ---------------------------------------------------


@admin.register(models.Example)
class PermissionCodeAdmin(root_models.CustomBaseAdmin):
    list_display = ['some', 'thing']
    list_filter = ['groups']
    search_fields = ['some', 'user__username']
    ordering = ['-id']
    readonly_fields = ['thing']
    filter_horizontal = ['groups']
    actions = [example_action]
