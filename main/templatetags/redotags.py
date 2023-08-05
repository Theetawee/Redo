from django import template
from django.shortcuts import redirect

register=template.Library()

@register.filter
def redo_class(field,css_class):
    try:
        if css_class:
            field.field.widget.attrs['class']=css_class
            
        return field
    except:
        return 'Error'


@register.filter
def redo_holder(field,placeholder):
    try:
        if placeholder:
            field.field.widget.attrs['placeholder']=placeholder
            
        return field
    except:
        return 'Error'