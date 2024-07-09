# shop/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def get_val(num):
    return range(num)
