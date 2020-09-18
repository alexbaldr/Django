from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    main_url = reverse('bus_stations')
    bus_list = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_list.append(row)

    paginator = Paginator(bus_list, 10)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)
    previous_page_url, next_page_url = None, None
    if page_obj.has_previous():
        previous_page_url = main_url + f'?page={page_obj.previous_page_number()}'
    if page_obj.has_next():
        next_page_url = main_url + f'?page={page_obj.next_page_number()}'
    return render_to_response('index.html', context={
                'bus_stations': page_obj,
                'current_page': page_number,
                'prev_page_url': previous_page_url,
                'next_page_url': next_page_url,
            })
