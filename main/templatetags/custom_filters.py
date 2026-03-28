from django import template

register = template.Library()

@register.filter
def get_unit(note, i):
    return getattr(note, f'unit{i}', None)

