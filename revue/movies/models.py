from django.db import models
from django.conf import settings
from datetime import datetime
from taggit.managers import TaggableManager

# Create your models here.

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
AGE_CHOICES = (
    ('10', '20살 미만'),
    ('20', '20대'),
    ('30', '30대'), 
    ('40', '40대'),
    ('50', '50대 이상')
)

class Genre(models.Model):
    kname = models.CharField(max_length = 20)
    ename = models.CharField(max_length = 20)
    def __str__(self):
        return self.kname

class Movie(models.Model):
    ktitle = models.CharField(max_length = 50)
    etitle = models.CharField(max_length = 50)
    original_title = models.CharField(max_length=70)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    koverview = models.TextField()
    eoverview = models.TextField()
    original_language = models.CharField(max_length = 20)
    poster_path = models.CharField(max_length= 50, null=True)
    backdrop_path = models.CharField(max_length = 50, null=True)
    genres = models.ManyToManyField(Genre, related_name = 'in_movies')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies')
    tags = TaggableManager()

    def __str__(self):
        return f'{self.ktitle}'


class Genre_counter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete= models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    counter = models.PositiveIntegerField(default = 1)
    
class Gender_age_counter(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ages = models.CharField(max_length=2, choices=AGE_CHOICES)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    counter = models.PositiveIntegerField(default = 1)



class Trending(models.Model):
    movies = models.ManyToManyField(Movie, related_name='istrending')
    trendingdate = models.DateField(auto_now_add = True)
