from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def output_if_active(context, output, urls):
    if context["request"].path in (reverse(url) for url in urls.split()):
        return output
    return ""
