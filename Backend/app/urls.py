# from django.urls import path
from .views import ActorsListView

from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('actors/',ActorsListView.as_view()),
]