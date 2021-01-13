# from django.urls import path

# from .views import NewsViewSet

# urlpatterns = [
#     path('', NewsListView.as_view()),
#     path('create/', NewsCreateView.as_view())
# ]


from .views import NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', NewsViewSet, basename='user')
urlpatterns = router.urls
