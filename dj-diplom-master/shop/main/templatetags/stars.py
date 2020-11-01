from django. template import library

register = library.Library()

@register.filter
def stars_filter(value):
    if(value) == 5:
        return " ★★★★★ "
    elif(value) == 4:
        return " ★★★★ "
    elif(value) == 3:
        return " ★★★ "
    elif(value) == 2:
        return " ★★ "
    elif(value) == 1:
        return " ★ "