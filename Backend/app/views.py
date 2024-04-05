
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer,ActorSerializer
from .models import Movie,Actor,Review
from django.db.models import Avg
import json

    
class ActorsListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
class MoviesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class MoviesListView(ListAPIView):
    queryset = Movie.objects.all().annotate(average=Avg('review__grade'))
    serializer_class = MovieSerializer
    pagination_class= MoviesPagination
    
class MovieUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class ReviewView(APIView):
    def post(self,request,pk):
        data = json.loads(request.body)
        m = Movie.objects.get(id=pk)
        Review.objects.create(grade=data["grade"],movie=m)
        average=Review.objects.filter(movie_id=pk).aggregate(Avg('grade'))
        return Response(average)
    

    
