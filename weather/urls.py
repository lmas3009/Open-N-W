from django.urls import path
from .views import Latest_Weather, Latest_Country_Weather

urlpatterns = [
    path('API=<str:api>&Lat=<str:lat>&Lon=<str:lon>/', Latest_Weather),
    path('API=<str:api>&Country=<str:name>,<str:id>', Latest_Country_Weather),
]
