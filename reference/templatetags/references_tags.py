from django import template
from ..models import Reference

from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag()
def total_posts():
    return Reference.published.count()

@register.inclusion_tag('reference/reference_list/latest_references.html')
def show_latest_references(count=5):
    latest_references = Reference.objects.order_by('-publish')[:count]
    return {'latest_references': latest_references}
