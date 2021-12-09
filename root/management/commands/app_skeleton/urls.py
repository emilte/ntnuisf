# imports
from django.urls import path

from . import views
# End: imports -----------------------------------------------------------------

app_name = 'app_skeleton'  # Necessary for url naming. eg {% url 'app_skeleton:view_profile' %}

urlpatterns = [
    path('example/<int:example_id>/', views.ExampleView.as_view(), name='view_profile'),
]
