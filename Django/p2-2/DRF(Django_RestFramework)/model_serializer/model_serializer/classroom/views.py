from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import models

# 序列化类
class ClassroomSerializer(serializers.Serializer):
    roomname = serializers.CharField()
    roomuse = serializers.CharField()
    roomdesc = serializers.CharField()
    createtime = serializers.DateTimeField()
    updatetime = serializers.DateTimeField()
    
class ClassRoomView(APIView):
    def get(self, request):
        clslist = models.ClassModel.objects.all()
        clsserializer = ClassroomSerializer(clslist, many=True)
        return Response(clsserializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     return Response('CLS POST请求'+request.data['clsname'])