from django.db import models
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
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    