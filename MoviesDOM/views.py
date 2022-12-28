# from django.http import JsonResponse
# from blog.models import PopularMovie, ComedyMovie, ActionMovie
# from .serializers import PopularMoviesSerializer, ComedyMoviesSerializer, ActionMoviesSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST'])
# def popular_movies_list(request):
#     if request.method == 'GET':
#         pm_list = PopularMovie.objects.all()
#         serializer = PopularMoviesSerializer(pm_list, many=True) 
#         return JsonResponse({'popular movie': serializer.data}, safe=False)
    
#     if request.method == 'POST':
#         serializer = PopularMoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

        
# def comedy_movies_list(request):
#     cm_list = ComedyMovie.objects.all()
#     serializer = ComedyMoviesSerializer(cm_list, many=True) 
#     return JsonResponse({'comedy movie': serializer.data}, safe=False)

# def action_movies_list(request):
#     am_list = ActionMovie.objects.all()
#     serializer = ActionMoviesSerializer(am_list, many=True) 
#     return JsonResponse({'action movie': serializer.data}, safe=False)