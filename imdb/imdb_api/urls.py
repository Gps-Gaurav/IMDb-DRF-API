from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('list/', views.movie_list, name='movie_list'),
    # path('list/<int:pk>', views.movie_detail, name='movie_detail'),
    path('stream', views.StreamPlatformList.as_view(), name='stream_list'),
    path('stream/<int:pk>', views.StreamPlatformDetail.as_view(), name='stream_detail')
    
]
urlpatterns = format_suffix_patterns(urlpatterns)