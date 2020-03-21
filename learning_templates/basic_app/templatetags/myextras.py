from django import template

register = template.Library()

 # 2nd way to use custom filter
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all value of "arg" from the String!

    """
    return value.replace(arg,'')

#register.filter('cut',cut)# first way to use custom filter
