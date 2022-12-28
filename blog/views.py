from django.shortcuts import get_object_or_404, render
from .models import PopularMovie, ComedyMovie, ActionMovie, MyList
from django.http import JsonResponse
from blog.models import PopularMovie, ComedyMovie, ActionMovie
from .serializers import PopularMoviesSerializer, ComedyMoviesSerializer, ActionMoviesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets



def index(request):
    return render(request, 'index.html')


class PopularMoviesViewSet(viewsets.ViewSet):
    queryset = PopularMovie.objects.all()
    serializer_class = PopularMoviesSerializer

    def list(self, request):
        queryset = PopularMovie.objects.all()
        serializer = PopularMoviesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PopularMovie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = PopularMoviesSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        serializer = PopularMoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        movie = PopularMovie.objects.get(pk=pk)
        serializer = PopularMoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        movie = PopularMovie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)

class ComedyMoviesViewSet(viewsets.ViewSet):
    queryset = ComedyMovie.objects.all()
    serializer_class = ComedyMoviesSerializer

    def list(self, request):
        queryset = ComedyMovie.objects.all()
        serializer = ComedyMoviesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ComedyMovie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = ComedyMoviesSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        serializer = ComedyMoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        movie = ComedyMovie.objects.get(pk=pk)
        serializer = ComedyMoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        movie = ComedyMovie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)

class ActionMoviesViewSet(viewsets.ViewSet):
    queryset = ActionMovie.objects.all()
    serializer_class = ActionMoviesSerializer

    def list(self, request):
        queryset = ActionMovie.objects.all()
        serializer = ActionMoviesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ActionMovie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = ActionMoviesSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        serializer = ActionMoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        movie = ActionMovie.objects.get(pk=pk)
        serializer = ActionMoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        movie = ActionMovie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)

def about(request):
    # context = {
    #     'myList': MyList.objects.all(),
    # }
    return render(request, 'description.html')


    

