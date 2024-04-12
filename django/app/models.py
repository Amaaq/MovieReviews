from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title


class Review(models.Model):
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.grade} for {self.movie.title}"
