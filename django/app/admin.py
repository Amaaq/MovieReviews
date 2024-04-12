from django.contrib import admin

from .models import Actor, Movie, Review

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Actor)
