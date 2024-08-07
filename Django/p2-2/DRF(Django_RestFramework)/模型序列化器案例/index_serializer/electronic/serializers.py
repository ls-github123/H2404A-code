from wsgiref.validate import validator
from . import models
from rest_framework import serializers

class ElecSerializer(serializers.Serializer):
    # required=False 将所属字段设置为非必填项
    id = serializers.CharField(required=False)
    name = serializers.CharField() # 部件名称
    usability = serializers.CharField() # 可用性
    specification = serializers.CharField() # 规格
    createtime = serializers.DateField() # 入库时间
    
    class Meta:
        model = models.ElectronicModel
        fields = "__all__" # 返回所有字段
    
    # 模型序列器无法自动执行create()操作
    # 手动重写create()方法
    def create(self, validated_data):
        return models.ElectronicModel.objects.create(**validated_data)
    
    # 模型序列化器无法自动执行update()操作
    # 手动重写update()方法
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.usability = validated_data.get('usability', instance.usability)
        instance.specification = validated_data.get('specification', instance.specification)
        instance.createtime = validated_data.get('createtime', instance.createtime)
        instance.save()
        return instance