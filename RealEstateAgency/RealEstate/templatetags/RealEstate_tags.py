from django import template
from RealEstate.models import RealEstate, Categories
from django.db.models import *
register = template.Library()



@register.simple_tag()
def state():
    return RealEstate.objects.all()

@register.inclusion_tag('RealEstate/list_categories.html')
def show_categories():
    cat = Categories.objects.annotate(c=Count('realestate').filter(c__gt=0))
    return{'cat':cat}

@register.simple_tag()
def category():
    return Categories.objects.all()