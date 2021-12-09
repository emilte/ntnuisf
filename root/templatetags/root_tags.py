# imports
import random

from django import template
from django.conf import settings
from django.utils import timezone
from django.templatetags.static import static

# End: imports -----------------------------------------------------------------

register = template.Library()

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/


@register.simple_tag
def get_image(model, fieldname):
    if not model or not getattr(model, fieldname):
        return static('/root/img/image-placeholder.png')
    return getattr(model, fieldname).url


@register.simple_tag
def divide(arg1, arg2):
    try:
        return round(int(arg1) / int(arg2), 1)
    except (ValueError, ZeroDivisionError):
        return 0


@register.simple_tag
def random_choice(iterable):
    return random.choice(iterable)


# settings value
@register.simple_tag(name='get_settings')
def get_settings(var_name):
    """
    Usage:
        {% settings_value 'LANGUAGE_CODE' %}
    """
    return getattr(settings, var_name, '')


@register.simple_tag(name='marked_by')
def marked_by(interactable, user):
    """
    Usage:
        {% marked_by interactable user as (type of intraction, example favorite) %}
    """
    if not interactable and not user:
        raise Exception('interactable is required')
    if not user:
        raise Exception('user is required')

    return interactable.is_marked_by(user)


@register.simple_tag(name='reacted_by')
def reacted_by(interactable, user):
    """
    Usage:
        {% reacted_by interactable user as (type of intraction, example liked) %}
    """
    if not interactable and not user:
        raise Exception('interactable is required')
    if not user:
        raise Exception('user is required')

    return interactable.is_reacted_by(user)


@register.filter(name='times')
def times(number):
    """Enables in-range for-loops within templates given a number"""
    return range(number)


@register.filter(name='since')
def time_since_datetime(datetime):
    seconds = (timezone.now() - datetime).total_seconds()
    if seconds < 60 * 2:
        return 'Akkurat nå'
    if seconds < 60 * 60:
        return f'{int(seconds//60)} minutter siden'
    if seconds < 60 * 60 * 24:
        return f'{int(seconds//3600)} timer siden'
    if seconds < 60 * 60 * 24 * 3:
        return f'{int(seconds//86400)} dager siden'
    return datetime


# https://stackoverflow.com/questions/16348003/displaying-a-timedelta-object-in-a-django-template
@register.filter()
def smooth_timedelta(timedeltaobj):
    """Convert a datetime.timedelta object into Days, Hours, Minutes, Seconds."""
    if not timedeltaobj:
        return None
    secs = timedeltaobj.total_seconds()
    timetot = ''
    if secs > 86400:  # 60sec * 60min * 24hrs
        days = secs // 86400
        timetot += f'{int(days)} dager'
        secs = secs - days * 86400

    if secs > 3600:
        hrs = secs // 3600
        timetot += f' {int(hrs)} timer'
        secs = secs - hrs * 3600

    if secs > 60:
        mins = secs // 60
        timetot += f' {int(mins)} minutter'
        secs = secs - mins * 60

    if secs > 0:
        timetot += f' {int(secs)} sekunder'
    return timetot
