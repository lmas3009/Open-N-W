# from django.urls import path

# from .views import NewsViewSet

# urlpatterns = [
#     path('', NewsListView.as_view()),
#     path('create/', NewsCreateView.as_view())
# ]


# from .views import NewsViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', NewsViewSet, basename='user')
# urlpatterns = router.urls


from django.urls import path
from .views import Latest_News,Indexed_id,Latest_Country_News

urlpatterns=[
    path('API=<str:api>&Country=<str:name>/',Latest_Country_News),
    path('API=<str:api>&Countrycode=<str:name>&Id=<int:id>/',Indexed_id)
]