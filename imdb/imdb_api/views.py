from django.http import HttpResponse, JsonResponse
from django.http import Http404

from .models import WatchList, StreamPlatform, reviews
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
#  using generic class

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('movie_list', request=request, format=format),
        'streamplatforms': reverse('stream_list', request=request, format=format)
    })
    

class streamPlatformViewset(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class review_list(generics.ListCreateAPIView):
    """
    This ViewSet automatically provides `list` and `create` actions.
    """
    queryset = reviews.objects.all()
    serializer_class = ReviewSerializer
    

class review_detail( generics.RetrieveUpdateDestroyAPIView):
    """
    This ViewSet automatically provides `retrieve`, `update` and `destroy` actions.
    """
    queryset = reviews.objects.all()
    serializer_class = ReviewSerializer
            
    
# class StreamPlatformList(generics.ListCreateAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def perform_create(self, serializer):
#         serializer.save()  # You can add custom logic here if needed

# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer


# #using mixins

# class StreamPlatformList(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class StreamPlatformDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#     lookup_field = 'pk'
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# # using generic views
# # class based views
# class StreamPlatformList(APIView):
#     def get(self, request, format=None):
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)

#     def post(self, request, format= None):
#         serialized = StreamPlatformSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, format=None):
#         serialized = StreamPlatformSerializer(data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete (self, request, format=None):
#         stream_platform = StreamPlatform.objects.all()
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class StreamPlatformDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         stream_platform = self.get_object(pk)
#         serialized = StreamPlatformSerializer(stream_platform)
#         return Response(serialized.data)


#     def put(self, request, pk, format=None):
#         serialized = StreamPlatformSerializer(StreamPlatform, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         stream_platform = self.get_object(pk)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

# # function based views

@api_view(['GET'])
def movie_list(_):
    movie_list = WatchList.objects.all()
    serialized = WatchListSerializer(movie_list, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def movie_detail(_, pk):
    movie = WatchList.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return Response(serialized.data)

# @api_view(['GET', 'POST'])
# def stream_list(request, format = None):
#     if request.method == 'GET':
#        stream_list = StreamPlatform.objects.all()
#        serialized = StreamPlatformSerializer(stream_list, many=True)
#        return Response(serialized.data)
#     elif request.method == 'POST':
#        data=request.data
#        serialized = StreamPlatformSerializer(data=request.data)
#        if serialized.is_valid():
#            serialized.save()
#            return Response(serialized.data, status=status.HTTP_201_CREATED)
#        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request, pk , format = None):   
#     try:
#         stream = StreamPlatform.objects.get(pk=pk)
#     except StreamPlatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#     # If the request method is GET, return the stream details
#         serialized = StreamPlatformSerializer(stream)
#         return Response(serialized.data)
#     elif request.method == 'PUT':
#         # If the request method is PUT, update the stream details
#         serialized = StreamPlatformSerializer(stream, data=request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         # If the request method is DELETE, delete the stream
#         stream.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)