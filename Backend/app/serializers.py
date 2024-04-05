from .models import Actor,Movie
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

        
class MovieSerializer(serializers.ModelSerializer):
    average= serializers.DecimalField(max_digits=3,decimal_places=2)
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'