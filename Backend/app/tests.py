from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie,Actor,Review

class MovieViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor1 = Actor.objects.create(first_name='actor1',last_name='actor1')
        self.actor2 = Actor.objects.create(first_name='actor2',last_name='actor2')
        self.actor3 = Actor.objects.create(first_name='actor3',last_name='actor3')
        self.movie1 = Movie.objects.create(title="Test Movie 1", description="Test Description 1")
        self.movie2 = Movie.objects.create(title="Test Movie 2", description="Test Description 2")
        self.movie1.actors.set([self.actor1,self.actor2])
        self.movie2.actors.set([self.actor2,self.actor3])
        self.review1_movie1=Review.objects.create(movie=self.movie1,grade=2)
        self.review2_movie1=Review.objects.create(movie=self.movie1,grade=4)
        self.review1_movie2=Review.objects.create(movie=self.movie2,grade=1)
        self.review2_movie2=Review.objects.create(movie=self.movie2,grade=3)

    def test_list_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test number of movies
        self.assertEqual(response.data['count'], Movie.objects.count())

        # Test Expected Data
        movie_titles = [movie['title'] for movie in response.data['results']]
        self.assertIn(self.movie1.title, movie_titles)
        self.assertIn(self.movie2.title, movie_titles)
            
    def test_movie_details(self):
        response=self.client.get('/movies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test Expected Data 
        self.assertEqual(response.data['title'],self.movie1.title)
        self.assertEqual(response.data['description'],self.movie1.description)
        self.assertEqual(len(response.data['actors']),len([self.actor1,self.actor2]))
        self.assertEqual(response.data['average'],3)
        
    def test_movie_update(self):
        response= self.client.patch('/movies/2/',payload={"description":"Updated Description","actors":[1]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['title'],self.movie2.title)
        self.assertEqual(response.data['description'],self.movie2.description)
        self.assertEqual(response.data['actors'][0]['id'],self.actor2.id)
        self.assertEqual(response.data['average'],2)
        
    def test_add_review(self):
        response = self.client.post('/movies/2/add_review/',{"grade":2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Test if Review is added 
        self.assertEqual(self.movie2.review_set.count(),3)
        
        # Test Expected Data
        self.assertEqual(response.data['title'],self.movie2.title)
        self.assertEqual(response.data['description'],self.movie2.description)
        self.assertEqual(len(response.data['actors']),len([self.actor2,self.actor3]))
        self.assertEqual(response.data['average'],2)
        
class ActorsListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor1 = Actor.objects.create(first_name='actor1',last_name='actor1')
        self.actor2 = Actor.objects.create(first_name='actor2',last_name='actor2')
        self.actor3 = Actor.objects.create(first_name='actor3',last_name='actor3')
        self.actor4 = Actor.objects.create(first_name='actor4',last_name='actor4')
        self.actor5 = Actor.objects.create(first_name='actor5',last_name='actor5')
        self.actor6 = Actor.objects.create(first_name='actor6',last_name='actor6')
        
    def test_list_actors(self):
        response = self.client.get('/actors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test number of movies
        self.assertEqual(len(response.data), Actor.objects.count())

        # Test Expected Data
        actors_list = [actor['id'] for actor in response.data]
        self.assertIn(self.actor1.id, actors_list)
        self.assertIn(self.actor2.id, actors_list)
        self.assertIn(self.actor3.id, actors_list)
        self.assertIn(self.actor4.id, actors_list)
        self.assertIn(self.actor5.id, actors_list)
        self.assertIn(self.actor6.id, actors_list)
    
