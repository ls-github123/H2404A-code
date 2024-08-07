from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.forms import ValidationError
from . import models

# 写一个校验函数 验证教室名称的唯一性
def Checkname(data):
    res = models.ClassModel.objects.filter(roomname=data)
    if res:
        # 表中已有数据
        raise ValidationError('教室名称已存在')
    else:
        return data

# 序列化类
class ClassroomSerializer(serializers.Serializer):
    roomname = serializers.CharField(validators=[Checkname])
    roomuse = serializers.CharField()
    roomdesc = serializers.CharField()
    createtime = serializers.DateTimeField()
    updatetime = serializers.DateTimeField()
    # 重写普通序列化器create方法
    # validated_data 被序列化类校验成功后的数据存储在其中
    def create(self, validated_data):
        # 执行添加 {'id1':'value1','id2':'value2'}  
        # **拆散字典对象 id1=validated_data['id1'] id2=validated_data['id2']
        cls = models.ClassModel.objects.create(**validated_data)
        if cls:
            return cls
        else:
            raise ValidationError('创建数据失败')
    
class ClassRoomView(APIView):
    def get(self, request):
        clslist = models.ClassModel.objects.all()
        clsserializer = ClassroomSerializer(clslist, many=True)
        return Response(clsserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        ser = ClassroomSerializer(data=request.data)
        if ser.is_valid():
            # 校验成功,调用序列化提供的save()方法 执行重写的create()方法
            ser.save()
            return Response(ser.data, status=201)
        else:
            return Response(ser.errors, status=202)
            
    def delete(self, request, pk):
        try:
            # 使用filter 如果条件不满足 返回一个空集合但不报错 不报错就捕获不到异常-即不触发对象不存在
            clsdel = models.ClassModel.objects.get(id=pk).delete()
            if clsdel:
                return Response({'msg':'删除成功!'})
            else:
                return Response({'msg':'删除失败!'})
        except models.ClassModel.DoesNotExist:
            raise NotFound(detail='对象不存在')
