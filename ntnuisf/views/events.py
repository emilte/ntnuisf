# imports
from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from ..views import wiki as wiki_views
from ..forms import events as event_forms
from ..models import events as event_models

# End: imports -----------------------------------------------------------------


@method_decorator([login_required, permission_required('events.add_event', login_url='forbidden')], name='dispatch')
class AddEventView(wiki_views.GenericAddModel):
    template = 'ntnuisf/events/event_form.html'
    form_class = event_forms.EventForm
    redirect_name = 'events:event_view'
    redirect_id = 'id'


@method_decorator([login_required, permission_required('events.change_event', login_url='forbidden')], name='dispatch')
class EditEventView(wiki_views.GenericEditModel):
    template = 'ntnuisf/events/event_form.html'
    form_class = event_forms.EventForm
    redirect_name = 'events:event_view'
    redirect_id = 'id'
    model = event_models.Event


@method_decorator([login_required], name='dispatch')
class AllEventsView(View):
    template = 'ntnuisf/events/all_events.html'
    form = event_forms.EventFilterForm

    def get(self, request: HttpRequest):
        events = event_models.Event.objects.all()
        form = self.form()
        return render(request, self.template, {'form': form, 'events': events})

    def post(self, request: HttpRequest):
        events = event_models.Event.objects.all()
        form = self.form(data=request.POST)
        if form.is_valid():
            events = self.event_filter(form=form, queryset=events)
        return render(request, self.template, {'form': form, 'events': events})

    def event_filter(self, *, form, queryset):  # pylint: disable=no-self-use
        search = form.cleaned_data['search']
        tag = form.cleaned_data['tag'] or None
        lead = form.cleaned_data['lead'] or None
        follow = form.cleaned_data['follow'] or None
        bulk = form.cleaned_data['bulk']
        day = form.cleaned_data['day']
        semester_char = form.cleaned_data['semester_char']

        if search != '':
            queryset = queryset.filter(title__icontains=search)
        if tag:
            queryset = queryset.filter(tags__id=tag)
        if lead:
            queryset = queryset.filter(lead=lead)
        if follow:
            queryset = queryset.filter(follow=follow)
        if bulk:
            queryset = queryset.filter(bulk=bulk)
        if day:
            queryset = queryset.filter(day=day)
        if semester_char:
            queryset = queryset.filter(semester_char=semester_char)

        return queryset


@method_decorator([login_required], name='dispatch')
class EventView(View):
    template = 'ntnuisf/events/event_view.html'

    def get(self, request: HttpRequest, event_id):
        event = event_models.Event.objects.get(id=event_id)
        return render(request, self.template, {'event': event})


@method_decorator([login_required], name='dispatch')
class EventSignup(View):

    def post(self, request: HttpRequest, model_id):
        event = event_models.Event.objects.get(id=model_id)
        p, created = event_models.Participant.objects.get_or_create(
            user=request.user,
            event=event,
        )

        if created:
            if event.participants.all().count() <= event.earlybirds:
                p.is_earlybird = True
                p.save()

        return redirect('events:event_view', model_id)
