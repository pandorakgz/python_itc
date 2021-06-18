from django.shortcuts import render
import requests
import json

# Create your views here.

covid_url = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'

def home(request):
    return render(request, 'home_covid.html')

def get_covid(request):
    city_input = request.POST.get('city_input')
    pf = covid_url.format(country = city_input)
    po = requests.get(pf)
    po_j=po.json()
    temp = po_j["All"]["confirmed"],
    temp1=po_j["All"]["recovered"],
    temp2 = po_j["All"]["deaths"],
    temp3 = po_j["All"]["country"],
    temp4 = po_j["All"]["sq_km_area"],
    temp5 = po_j["All"]["life_expectancy"],



    return render(request, 'home_covid.html',{
        'pf':pf,
        'po_j':po_j,
        'temp':temp,
        'temp1':temp1,
        'temp2':temp2,
        'temp3':temp3,
        'temp4':temp4,
        'temp5':temp5,

        'city_input': city_input,
    })