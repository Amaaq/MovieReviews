from django.urls import path
from .views import MovieList,ActorList
urlpatterns = [
    path('movies/',MovieList.as_view()),
    path('actors/',ActorList.as_view()),
]