from rest_framework import serializers
from . import models

class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MesCateModel
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):
    cate = serializers.StringRelatedField()
    class Meta:
        model = models.MessageModel
        fields = '__all__'
        
class MessageAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageModel
        fields = '__all__'