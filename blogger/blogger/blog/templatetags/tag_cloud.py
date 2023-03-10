from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("blog/components/tag-cloud.html")
def sidebard_tag_cloud():
    x = Tag.objects.all()
    return {"tags": x}

