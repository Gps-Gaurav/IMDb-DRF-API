from rest_framework import serializers
from .models import  WatchList, StreamPlatform
 
# model based serializers
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
    # fields = ['id', 'title', 'storyline', 'platform', 'active', 'created_at', 'updated_at']

# non-model based serializers

# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     storyline = serializers.CharField(max_length=255)
#     # platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
#     active = serializers.BooleanField(default=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
    
#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.save()
#         return instance
    
# # model based serializers
# class StreamPlatformSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'
# # usinng hyperlink
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchList= WatchListSerializer(many=True, read_only=True)
    # watchList = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist-detail', lookup_field='pk')
    # watchlist = serializers.StringRelatedField( many=True, read_only=True)
    # link = serializers.HyperlinkedIdentityField(view_name='streamplatform-detail', format='html' )
    class Meta:
        model = StreamPlatform
        fields = '__all__'
   
# non-model based serializers

# class StreamPlatformSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     about = serializers.CharField(max_length=255)
#     website = serializers.URLField(max_length=200)    
    
#     def create(self, validated_data):
#         return StreamPlatform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance
    
