
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieSerializer, MovieListSerializer,ReviewSerializer,ActorSerializer
from .models import Movie,Actor

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return MovieListSerializer  # Utiliser le sérialiseur de liste pour la vue de liste
#         return MovieSerializer  # Utiliser le sérialiseur par défaut pour les autres actions

    # @action(detail=True, methods=['post'])
    # def add_acteur_ou_avis(self, request, pk=None):
    #     movie = self.get_object()
    #     type = request.data.get('type')
    #     if type == 'actor':
    #         actor_id = request.data.get('actor_id')
    #         try:
    #             acteur = Actor.objects.get(pk=actor_id)
    #         except Actor.DoesNotExist:
    #             return Response({'message': 'Acteur non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    #         movie.acteurs.add(acteur)
    #         return Response({'message': 'Acteur ajouté avec succès au film'})
    #     elif type == 'review':
    #         grade = request.data.get('grade')
    #         Review.objects.create(movie=film, grade=grade)
    #         average = Movie.reviews.aggregate(average=Avg('grade'))['average']
    #         return Response({'message': 'Avis ajouté avec succès', 'average': average}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'message': 'Type invalide'}, status=status.HTTP_400_BAD_REQUEST)

class MoviesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class= MoviesPagination
    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer 
        return MovieSerializer

    def update(self, request,*args,**kwargs):
        movie = self.get_object()

        if 'actors' in request.data:
            new_actors_list = request.data.pop('actors')
            movie.actors.clear()
            movie.actors.add(*new_actors_list)

        serializer = self.get_serializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        movie = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            movie_serializer = MovieSerializer(movie)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ActorsListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer