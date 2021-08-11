from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# from django.utils.text import slugify
from django.template import defaultfilters
from unidecode import unidecode



# Create your models here.
class Movie(models.Model):
    movie = models.CharField(max_length=10)
    hall = models.CharField(max_length=10)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Vacancy = models.IntegerField(default=1)
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
