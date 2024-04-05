
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer,ActorSerializer
from .models import Movie,Actor
from django.db.models import Avg

class MoviesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class MovieList(ListAPIView):
    serializer_class = MovieSerializer
    pagination_class= MoviesPagination
    def get_queryset(self):
        queryset = Movie.objects.all().annotate(average=Avg('review__grade'))
        return queryset
    
    
class ActorList(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    
