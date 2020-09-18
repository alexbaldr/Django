from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_catalog = request.GET.get('sort')
    if sort_catalog:
        if 'name' in sort_catalog:
            order = Phone.objects.order_by('name')
        elif "min_price" in sort_catalog:
            order = Phone.objects.order_by('price')
        elif "max_price" in sort_catalog:
            order = Phone.objects.order_by('-price')   
    else:
        order = Phone.objects.all() 

    context = {
        "phones": order,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html' 
    phone = Phone.objects.get(slug=slug)
    context = {
        'phones': phone,
    }
    return render(request, template, context)
