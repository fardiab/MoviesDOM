from django.contrib import admin
from .models import PopularMovie, ComedyMovie, ActionMovie


admin.site.register(PopularMovie)
class PopularMovieAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(ComedyMovie)
class ComedyMovieAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(ActionMovie)
class ActionMovieAdmin(admin.ModelAdmin):
    list_display = ('title')
    