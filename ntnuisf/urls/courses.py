# imports
from django.urls import path
from ..views import courses as course_views
# End: imports -----------------------------------------------------------------

app_name = 'courses'

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('all/', course_views.AllCoursesView.as_view(), name='all_courses'),
    path('add/', course_views.AddCourseView.as_view(), name='add_course'),
    path('<int:course_id>/', course_views.CourseView.as_view(), name='course_view'),
    path('delete/<int:course_id>/', course_views.DeleteCourseView.as_view(), name='delete_course'),
    path('edit/<int:course_id>/', course_views.EditCourseView.as_view(), name='edit_course'),
    path('duplicate/<int:course_id>/', course_views.DuplicateCourse.as_view(), name='duplicate_course'),
    path('export/<int:course_id>/', course_views.ExportView.as_view(), name='export_course'),
    path('spotify/create_playlist/<int:course_id>/', course_views.CreatePlaylistView.as_view(), name='create_playlist'),
]
