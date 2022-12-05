from rest_framework import serializers
from blog.models import PopularMovie, ComedyMovie, ActionMovie


class PopularMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularMovie
        fields = ['id', 'image', 'title']

class ComedyMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComedyMovie
        fields = ['id', 'image', 'title']

class ActionMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionMovie
        fields = ['id', 'image', 'title']

