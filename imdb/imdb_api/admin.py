from django.contrib import admin
from .models import StreamPlatform, WatchList
from .models import reviews
# Register your models here.

admin.site.register(StreamPlatform)
admin.site.register(WatchList)
admin.site.register(reviews)