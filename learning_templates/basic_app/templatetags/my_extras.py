from django import template

register = template.Library()

@register.filter(name='mycut')
def mycut(value,arg):
    """
    This cuts out the arg from the value
    """
    return value.replace(arg,"")

# register.filter('mycut',mycut)

