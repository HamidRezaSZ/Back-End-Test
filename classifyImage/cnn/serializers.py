from rest_framework import serializers


class PictureSerializer(serializers.Serializer):
    
    picture = serializers.ImageField()