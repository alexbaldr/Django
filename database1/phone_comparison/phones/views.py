from django.shortcuts import render
from phones.models import Phone, Iphone, Xiomi, Sumsung
from django.views.generic import ListView


class PhoneListView(ListView):
    apple = Iphone.objects.all()[0]
    xiaomi = Xiomi.objects.all()[0]    
    samsung = Sumsung.objects.all()[0]

def show_catalog(request):
    
    template = 'catalog.html'
    phones = [PhoneListView.apple, PhoneListView.xiaomi, PhoneListView.samsung]

    context = {
        "phones": phones
    }
    return render(request, template, context)
