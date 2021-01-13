# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import News
# from .serializer import NewsSerializer


# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import News
from .serializer import NewsSerializer
from django.http import HttpResponse,HttpRequest,JsonResponse
import json
import urllib.request



# Create your views here.e2b1a670aa6c406a821291c1350e7b90


@csrf_exempt
def Latest_News(request,api):

    if(request.method=='GET'):
        url = ('http://newsapi.org/v2/top-headlines?'
            'country=us&'
            'apiKey='+api)
        response = urllib.request.urlopen(url).read().decode('UTF-8')
        data = json.loads(response)
        dat = data["articles"]
        return JsonResponse(dat,safe=False)

@csrf_exempt
def Latest_Country_News(request,name,api):
    print(name,api)
    if(request.method=='GET'):
        url = ('http://newsapi.org/v2/top-headlines?'
            'country='+name+'&'
            'apiKey='+api)
        print(url)
        response = urllib.request.urlopen(url).read().decode('UTF-8')
        data = json.loads(response)
        dat = data["articles"]
        return JsonResponse(dat,safe=False)
    
@csrf_exempt
def Indexed_id(request,id,api,name):
    print(api,name,id)
    if(request.method=='GET'):
        url = ('http://newsapi.org/v2/top-headlines?'
            'country='+name+'&'
            'apiKey='+api)
        response = urllib.request.urlopen(url).read().decode('UTF-8')
        data = json.loads(response)
        dat = data["articles"]
        return JsonResponse(dat[id],safe=False)
