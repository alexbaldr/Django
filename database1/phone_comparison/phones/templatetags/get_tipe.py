from django.template import library


register = library.Library()

@register.filter
def dash(value):
    if value == True:
        return "Есть"
    else:
        return "-"


@register.filter
def get_edge(value):
    split_list = value.split(',')
    return split_list
