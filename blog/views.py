from django.shortcuts import render
from .models import PopularMovie, ComedyMovie, ActionMovie


def index(request):
    context = {
        'popularMovies': PopularMovie.objects.all(),
        'comedyMovies': ComedyMovie.objects.all(),
        'actionMovies': ActionMovie.objects.all(),
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'description.html')

