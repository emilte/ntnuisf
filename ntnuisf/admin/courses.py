from django.contrib import admin

from ..models.courses import CourseSection, Course


@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'nr']
    list_display_links = ['title', 'course']
    ordering = ['course', 'nr']
    readonly_fields = ['course', 'nr', 'description']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'lead', 'follow', 'date', 'place']
    ordering = ['date', 'start']
    list_filter = ['tags']
    readonly_fields = ['created', 'last_edited', 'last_editor']
    filter_horizontal = ['tags', 'instructors']
    search_fields = ['title', 'place', 'lead__first_name', 'follow__first_name']

    # search_fields = ['instructors'] # test
    autocomplete_fields = ['instructors']  # test
