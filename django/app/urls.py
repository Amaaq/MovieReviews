# from django.urls import path
from rest_framework import routers

from django.urls import include, path

from .views import ActorsListView, MovieViewSet

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorsListView.as_view()),
]
