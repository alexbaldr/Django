from django.template import library
import csv


register = library.Library()


@register.filter
def get_color(value):

    with open ("inflation_russia.csv", encoding="utf-8") as fo:
        read_csv = list(csv.reader(fo))
    list_infl = [x.split(';') for b in read_csv[1:] for x in b]

    for name in list_infl:
        if value == name[0]:
            return "White"
        if value ==name[-1]:
            return "Grey"

    try:
        if float(value) < 0:
            return 'Green'
        elif   1.0 <= float(value) < 2.0:
            return "LightSalmon"
        elif  2.0 <= float(value) <5.0:
            return 'Salmon'
        elif float(value) >= 5.0:
            return 'Red'
    except:
        return "White"
