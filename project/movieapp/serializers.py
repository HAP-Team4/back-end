# movieapp/serializers.py

from rest_framework import serializers
from .models import Movie
from .models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'movie_id',
            'genre',
            'date',
            'time',
            'location',
            'capacity',
            'attendees'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'movie_list', 'attending')