from wsgiref.validate import validator
from 。 import models
from rest_framework import serializers

class EngiSerializer(serializers.ModelSerializer):
    # required=False 将所属字段设置为非必填项
    id = serializers.CharField(required=False)
    name = serializers.CharField() # 工程师姓名
    age = serializers.IntegerField() # 年龄
    professional = serializers.CharField() # 专业
    descinfo = serializers.CharField() # 个人简介
    
    class Meta:
        model = models.EngineerModel
        fields = "__all__" # 返回所有字段
    
    # # 模型序列器无法自动执行create()操作
    # # 手动重写create()方法
    # def create(self, validated_data):
    #     return models.EngineerModel.objects.create(**validated_data)
    
    # # 模型序列化器无法自动执行update()操作
    # # 手动重写update()方法
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.professional = validated_data.get('professional', instance.professional)
    #     instance.descinfo = validated_data.get('descinfo', instance.descinfo)
    #     instance.save()
    #     return instance
