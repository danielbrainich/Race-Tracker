from django import template
from datetime import date

register = template.Library()

@register.filter
def days_until(value):
    today = date.today()
    delta = value - today
    return (delta.days)

@register.filter
def calculate_percentile(value, total):
    try:
        if total > 0:
            return round((value / total) * 100, 2)
    except (ValueError, ZeroDivisionError):
        pass
    return 0
