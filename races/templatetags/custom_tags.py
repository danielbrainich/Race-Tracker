from django import template
from datetime import date

register = template.Library()

@register.filter
def calculate_percentile(value, total):
    try:
        if total > 0:
            return round((value / total) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    return 0
