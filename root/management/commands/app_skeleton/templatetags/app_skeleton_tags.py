# imports

from django import template

# End: imports -----------------------------------------------------------------

register = template.Library()

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/


@register.simple_tag(name='sum')
def example(a: int, b: int) -> int:
    return a + b


@register.filter(name='underscore_wrapper')
def wrapper(s: str):
    return f'_{s}_'
