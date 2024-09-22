from django import template
import datetime


register = template.Library()

@register.simple_tag(name= "get_the_date")
def get_the_date():
    return datetime.datetime.now()