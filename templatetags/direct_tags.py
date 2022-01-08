from django import template

register = template.Library()

@register.filter
def add_class(field, class_name):
    old_class_name = field.field.widget.attrs.get('class')
    field.field.widget.attrs.update({
        'class': f'{old_class_name} {class_name}' if old_class_name else class_name
    })
    return field

@register.filter
def is_match(model_url, page_url):
    return '/'.join(model_url.split('/')[:3]) == '/'.join(page_url.split('/')[:3])

