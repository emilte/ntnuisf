# imports
from django.urls import path

from ntnuisf.views import events
# End: imports -----------------------------------------------------------------

app_name = 'events'

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('all/', events.AllEventsView.as_view(), name='all_events'),
    path('add/', events.AddEventView.as_view(), name='add_event'),
    path('<int:event_id>/', events.EventView.as_view(), name='event_view'),
    path('edit/<int:model_id>/', events.EditEventView.as_view(), name='edit_event'),
    path('signup/<int:model_id>/', events.EventSignup.as_view(), name='event_signup'),
]
