from . import models
from rest_framework import serializers

# 使用模型序列器 ModelSerializer
# 自动完成 create及update操作
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.TaskModel
        fields = '__all__' # 返回所有字段