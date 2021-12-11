# imports
from django.urls import path

from ..views import info as info_views
# End: imports -----------------------------------------------------------------

app_name = 'info'

urlpatterns = [
    path('external/', info_views.external, name='external'),
    path('english/', info_views.english, name='english'),
    path('contact/', info_views.contact, name='contact'),
    path('about/', info_views.about, name='about'),
    path('hall_times/', info_views.hall_times, name='hall_times'),
    path('faq/', info_views.faq, name='faq'),
]
