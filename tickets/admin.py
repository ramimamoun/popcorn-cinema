from django.contrib import admin
from .models import Movie


# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    list_display = ['movie','hall','date','price','is_published']

admin.site.register(Movie,MovieAdmin)