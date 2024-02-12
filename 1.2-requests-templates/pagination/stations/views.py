import csv
from pagination.settings import BUS_STATION_CSV as path_csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

res_cont = list()
with open(path_csv, newline='', encoding="utf-8") as csvfile:
    content = csv.DictReader(csvfile)
    for i in content:
        d = {
            'Street':i.get('Street'),
            'Name':i.get('Name'),
            'District': i.get('District')
        }
        res_cont.append(d)



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(res_cont, 10)
    page_content = paginator.get_page(page_number)
    context = {
        'bus_stations': page_content,
        'page': page_content
    }
    return render(request, 'stations/index.html', context)