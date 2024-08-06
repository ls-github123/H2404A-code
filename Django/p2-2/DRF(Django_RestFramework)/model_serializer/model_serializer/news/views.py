from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import models

# 序列化类
class NewsSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    createtime = serializers.DateTimeField()
    
class NewsList(APIView):
    def get(self, request):
        newslist = models.NewsModel.objects.all()
        newsserializer = NewsSerializer(newslist, many=True)
        return Response(newsserializer.data, status=status.HTTP_200_OK)