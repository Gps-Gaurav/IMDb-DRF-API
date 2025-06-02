from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.decorators import api_view

stream_platform_list = views.streamPlatformViewset.as_view({
    'get': 'list',
    'post': 'create'
})
stream_platform_detail = views.streamPlatformViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('list/', views.movie_list, name='watchlist-list'),
    path('list/<int:pk>', views.movie_detail, name='watchlist-detail'),
    path('stream',stream_platform_list, name='streamplatform-list'),
    path('stream/<int:pk>',stream_platform_detail, name='streamplatform-detail'),
    path('', views.api_root, name='api_root'),
]
urlpatterns = format_suffix_patterns(urlpatterns)