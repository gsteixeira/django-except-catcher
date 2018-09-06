from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name='is_solved')
def is_solved(error):
    if error.resolved:
        ret = '<span class="green">Solved</span>'
    else:
        ret = '<span class="red">Unsolved</span>'
    return mark_safe(ret)
