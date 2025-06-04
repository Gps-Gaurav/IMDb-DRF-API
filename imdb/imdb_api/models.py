from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=255)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchList')
    av_rating = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
class reviews(models.Model):
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ])
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.CharField(max_length=255)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        string = str(self.rating) + " - " + self.watchlist.title
        return string
    
