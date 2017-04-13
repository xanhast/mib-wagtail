from django import template
from home.models import *
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.inclusion_tag('tags/teachers.html', takes_context=True)
def teachers(context):
    return {
        'teachers': Teacher.objects.all(),
        'request': context['request'],
    }

def obfuscate_string(value):
    return ''.join(['&#{0:s};'.format(str(ord(char))) for char in value])

@register.filter
@stringfilter
def obfuscate(value):
    return mark_safe(obfuscate_string(value))

# Retrieves the top menu items
@register.inclusion_tag('tags/nav.html', takes_context=True)
def nav(context, calling_page=None):
    menuitems = StandardPage.objects.live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }