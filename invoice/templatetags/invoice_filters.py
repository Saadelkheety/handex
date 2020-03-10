from django import template
from invoice.models import Product

register = template.Library()

@register.filter(is_safe=False)
def add(value, arg):
    """Add the arg to the value."""
    try:
        return round(float(value) + float(arg), 3)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def sub(value, arg):
    """Add the arg to the value."""
    try:
        return round(float(value) - float(arg), 3)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''


@register.simple_tag
def get_obj(pk, attr):
    obj = getattr(Product.objects.get(pk=int(pk)), attr)
    return obj
