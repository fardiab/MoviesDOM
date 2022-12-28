from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('popular-movies', views.PopularMoviesViewSet, basename='popular-movies')
router.register('comedy-movies', views.ComedyMoviesViewSet, basename='comedy-movies')
router.register('action-movies', views.ActionMoviesViewSet, basename='action-movies')

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('api/popular-movies/', views.PopularMoviesViewSet.as_view({'get': 'list'}), name='popular-movies'),
    path('api/popular-movies/<int:pk>/', views.PopularMoviesViewSet.as_view({'get': 'retrieve'}), name='popular-movies-detail'),
    path('api/popular-movies/create/', views.PopularMoviesViewSet.as_view({'post': 'create'}), name='popular-movies-create'),
    path('api/popular-movies/<int:pk>/update/', views.PopularMoviesViewSet.as_view({'put': 'update'}), name='popular-movies-update'),
    path('api/popular-movies/<int:pk>/delete/', views.PopularMoviesViewSet.as_view({'delete': 'destroy'}), name='popular-movies-delete'),
    path('api/comedy-movies/', views.ComedyMoviesViewSet.as_view({'get': 'list'}), name='comedy-movies'),
    path('api/comedy-movies/<int:pk>/', views.ComedyMoviesViewSet.as_view({'get': 'retrieve'}), name='comedy-movies-detail'),
    path('api/comedy-movies/create/', views.ComedyMoviesViewSet.as_view({'post': 'create'}), name='comedy-movies-create'),
    path('api/comedy-movies/<int:pk>/update/', views.ComedyMoviesViewSet.as_view({'put': 'update'}), name='comedy-movies-update'),
    path('api/comedy-movies/<int:pk>/delete/', views.ComedyMoviesViewSet.as_view({'delete': 'destroy'}), name='comedy-movies-delete'),
    path('api/action-movies/', views.ActionMoviesViewSet.as_view({'get': 'list'}), name='action-movies'),
    path('api/action-movies/<int:pk>/', views.ActionMoviesViewSet.as_view({'get': 'retrieve'}), name='action-movies-detail'),
    path('api/action-movies/create/', views.ActionMoviesViewSet.as_view({'post': 'create'}), name='action-movies-create'),
    path('api/action-movies/<int:pk>/update/', views.ActionMoviesViewSet.as_view({'put': 'update'}), name='action-movies-update'),
    path('api/action-movies/<int:pk>/delete/', views.ActionMoviesViewSet.as_view({'delete': 'destroy'}), name='action-movies-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
