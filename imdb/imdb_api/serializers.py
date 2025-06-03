from rest_framework import serializers
from .models import  WatchList, StreamPlatform, reviews
 
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
        
    
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value
    
    # object level validation
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError("Name and About cannot be the same.")
        return data
    
    # function based validation
    
#    
    # for serializers.Serializer
     
   
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
    
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
   
    class Meta:
        model = reviews
        fields = '__all__'
   
    # fields = ['id', 'rating', 'desc', 'watchlist', 'active', 'created_at', 'updated_at']   
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value