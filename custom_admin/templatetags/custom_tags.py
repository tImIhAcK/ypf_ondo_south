from atexit import register
from django import template
from ..models import State, Region, Participant, Convert
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag
def total_states():
    # Total number of registered state
    return State.objects.count()

@register.simple_tag
def total_region():
    # Total number of registered region
    return Region.objects.count()

@register.simple_tag
def total_participants():
    # Total number of registered state
    return Participant.objects.count()