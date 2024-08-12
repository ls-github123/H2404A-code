from rest_framework import serializers
from . import models

class ComputerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ComputerModel
        fields = '__all__' # 返回所有字段