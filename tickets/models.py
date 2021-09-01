from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# from django.utils.text import slugify
from django.template import defaultfilters
from django.contrib.auth.models import User
from unidecode import unidecode




# Create your models here.
Language =(
    ('Arabic','Arabic'),
    ('English','English'),
)


class Movie(models.Model):
    movie = models.CharField(max_length=10)
    hall = models.CharField(max_length=10)
    date = models.DateField()
    running_time = models.TimeField()
    des = models.TextField(max_length=500)
    Language = models.CharField(choices=Language,max_length=15)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Vacancy = models.IntegerField(default=1)
    Genre = models.CharField(max_length=10)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,null=True, allow_unicode=True)

    def __unicode__(self):
        return self.movie




    def save(self, *args, **kwargs):
        self.slug = slugify(self.movie)
        self.slug = defaultfilters.slugify(unidecode(self.movie))
        super(Movie,self).save(*args,**kwargs)

    def __str__(self):
        return self.movie
class Guest(models.Model):
    user = models.ForeignKey(User,related_name='gust_owner',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest,related_name='user_guest',on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name='reservation_movie',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)





