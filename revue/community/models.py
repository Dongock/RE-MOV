from django.db import models
from movies.models import Movie
from accounts.models import User
from django.conf import settings
from taggit.managers import TaggableManager
from datetime import datetime

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hits = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_reviews')
    tags = TaggableManager()
    



class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments')


class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_recomments')


class ShortReview(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_shorts')
    tags = TaggableManager()


class Report(models.Model):
    sort = models.CharField(max_length=50)
    r_id = models.IntegerField()
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    reason = (('욕','욕설'),('어그로','불쾌함을 주는 말'),('외설','외설적인 표현'), ('기타', '기타'))
    simple_reason = models.CharField(max_length=10, choices=reason)
    detail_reason = models.TextField()
    isresolved = models.BooleanField(default = False)
    reported_at = models.DateTimeField(auto_now_add=True)