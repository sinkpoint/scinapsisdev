from django import template

register = template.Library()

@register.filter
def author_format(value):
    if not value:
        return ''

    from django.utils.text import camel_case_to_spaces

    names = value.split(',')
    for i,n in enumerate(names):
        name = camel_case_to_spaces(n).split(' ')
        lastname = name[-1]
        init=''
        for j in range(len(name)-1):
            init += name[j][0].upper()
        fullname = init+' '+lastname.capitalize()
        names[i] = fullname
    return ', '.join(names)