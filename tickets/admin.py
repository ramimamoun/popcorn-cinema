from django.contrib import admin
from .models import Movie,Guest,Reservation


# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    list_display = ['movie','hall','date','price','is_published']

admin.site.register(Movie,MovieAdmin)
admin.site.register(Guest)
admin.site.register(Reservation)