from django import template

register=template.Library()

@register.filter
def redo_class(field,css_class):
    if css_class:
        field.field.widget.attrs['class']=css_class
        
    return field


@register.filter
def redo_holder(field,placeholder):
    if placeholder:
        field.field.widget.attrs['placeholder']=placeholder
        
    return field