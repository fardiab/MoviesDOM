from django.contrib import admin
from .models import PopularMovie, ComedyMovie, ActionMovie, MyList


admin.site.register(PopularMovie)
class PopularMovieAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(ComedyMovie)
class ComedyMovieAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(ActionMovie)
class ActionMovieAdmin(admin.ModelAdmin):
    list_display = ('title')
    
admin.site.register(MyList)
class MyListAdmin(admin.ModelAdmin):
    list_display = ('title')