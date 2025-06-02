from django.http import HttpResponse, JsonResponse
from .models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def movie_list(_):
    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list, many=True)
    return JsonResponse(serialized.data, safe=False)

def movie_detail(_, pk):
    movie = WatchList.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return JsonResponse(serialized.data, safe=False)

@api_view(['GET', 'POST'])
def stream_list(request, format = None):
    if request.method == 'GET':
       stream_list = StreamPlatform.objects.all()
       serialized = StreamPlatformSerializer(stream_list, many=True)
       return Response(serialized.data)
    elif request.method == 'POST':
       data=request.data
       serialized = StreamPlatformSerializer(data=request.data)
       if serialized.is_valid():
           serialized.save()
           return Response(serialized.data, status=status.HTTP_201_CREATED)
       return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def stream_detail(request, pk , format = None):   
    try:
        stream = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
    # If the request method is GET, return the stream details
        serialized = StreamPlatformSerializer(stream)
        return Response(serialized.data)
    elif request.method == 'PUT':
        # If the request method is PUT, update the stream details
        serialized = StreamPlatformSerializer(stream, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # If the request method is DELETE, delete the stream
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)