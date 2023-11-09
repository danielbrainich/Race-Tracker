from django import template
from datetime import date

register = template.Library()

@register.filter
def in_the_future(value):
    if value > date.today():
        return True

@register.filter
def days_until(value):
    today = date.today()
    delta = value - today
    return (delta.days)
