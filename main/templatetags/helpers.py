from django import template
register = template.Library()

@register.filter
def konvert(path, lang):
    return "/" + lang + path[3:]