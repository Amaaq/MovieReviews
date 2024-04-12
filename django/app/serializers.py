from rest_framework import serializers

from django.db.models import Avg

from .models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    average = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_average(self, obj):
        return obj.review_set.aggregate(moyenne=Avg("grade"))["moyenne"]


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["grade"]
