from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
import requests

# Create your views here.


@csrf_exempt
def Latest_Weather(request, api, lat, lon):
    print(api, lat, lon)
    request.is_secure() and "https" or "http"

    if(request.method == 'GET'):
        url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + \
            lat+'&lon='+lon+'&appid='+api
        response = requests.get(url)
        return JsonResponse(response.json(), safe=False, content_type="application/json")


@csrf_exempt
def Latest_Country_Weather(request, api, name, id):
    print(api, name)

    if(request.method == 'GET'):
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+name+','+id+'&appid='+api
        response = requests.get(url)
        return JsonResponse(response.json(), safe=False, content_type="application/json")
