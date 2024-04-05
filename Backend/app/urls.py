from django.urls import path
from .views import MoviesListView,ActorsListView,MovieUpdateView,ReviewView
urlpatterns = [
    path('movies/',MoviesListView.as_view()),
    path('actors/',ActorsListView.as_view()),
    path('movie/<int:pk>/',MovieUpdateView.as_view(),name='update_movie'),
    path('movie/<int:pk>/review',ReviewView.as_view(),name='add_review'),
]