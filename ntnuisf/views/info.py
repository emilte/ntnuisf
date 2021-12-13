# imports
from django.shortcuts import render

from ..models.info import Section
# End: imports -----------------------------------------------------------------


def external(request):
    section = Section.objects.get(title='Eksterne kurs')
    return render(request, 'ntnuisf/info/external.html', {'section': section})


def english(request):
    section = Section.objects.get(title='Information in English')
    return render(request, 'ntnuisf/info/english.html', {'section': section})


def contact(request):
    section = Section.objects.get(title='Kontakt oss')
    return render(request, 'ntnuisf/info/contact.html', {'section': section})


def about(request):
    section = Section.objects.get(title='Om oss')
    return render(request, 'ntnuisf/info/about.html', {'section': section})


def hall_times(request):
    section = Section.objects.get(title='Treningstider')
    return render(request, 'ntnuisf/info/hall_times.html', {'section': section})


def faq(request):
    section = Section.objects.get(title='FAQ')
    return render(request, 'ntnuisf/info/faq.html', {'section': section})
