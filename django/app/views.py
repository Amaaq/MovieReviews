from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Actor, Movie
from .serializers import (ActorSerializer, MovieListSerializer,
                          MovieSerializer, ReviewSerializer)
from .tasks import process


class MoviesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = MoviesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        if "actors" in request.data:
            new_actors_list = request.data.pop("actors")
            movie.actors.clear()
            movie.actors.add(*new_actors_list)

        serializer = self.get_serializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_review(self, request, pk=None):
        movie = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            result = process.delay()
            result.wait()
            movie_serializer = MovieSerializer(movie)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorsListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
