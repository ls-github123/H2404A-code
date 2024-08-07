from django.shortcuts import render # 用于渲染模板并返回一个 HttpResponse 对象
from rest_framework.views import APIView # 用于创建基于类的视图，专门用于处理 API 请求
from rest_framework.response import Response # 用于创建一个 HTTP 响应对象，包含序列化后的数据和 HTTP 状态码
from rest_framework.exceptions import NotFound # 用于引发 404 Not Found 异常
from . import models # 导入ORM数据模型
from . import serializers # 导入模型序列化器

# 该视图接口用于针对全部数据集进行增删改查处理
class EngiAllView(APIView):
    # 查询数据请求接口
    def get(self, request):
        # 获取所有数据
        alldata = models.EngineerModel.objects.all()
        # 序列化所有数据 [instance=所有数据]
        # many=True 参数仅在序列化查询集（即多个对象）时使用
        ser = serializers.EngiSerializer(instance=alldata, many=True)
        # 返回序列化后的数据
        return Response(ser.data, status=200)
    
    # 添加数据请求接口
    def post(self, request):
        # 反序列化数据 data=request.data
        ser = serializers.EngiSerializer(data=request.data)
        # 验证数据合规性
        # 合规-save() 不合规-errors
        if ser.is_valid():
            ser.save() # 自动处理创建
            return Response(ser.data, status=201)
        else:
            # 使用400表示客户端错误
            return Response(ser.errors, status=400)
    
    # 修改数据请求接口
    def put(self, request, id):
        try:
            data = models.EngineerModel.objects.get(id=id)
        except models.EngineerModel.DoesNotExist:
            raise NotFound(detail='要修改的数据不存在!')
        # instance 获取数据库中现有数据  data=request.data 获取修改后的数据
        # 两个条件必须同时写入时 才可执行update()方法 否则为create()操作
        ser = serializers.EngiSerializer(instance=data, data=request.data)
        if ser.is_valid():
            ser.save() # 触发保存
            return Response(ser.data, status=201)
        else:
            return Response(ser.data, status=400)
    
    # 删除数据请求接口
    def delete(self, request, id):
        try:
            elecdel = models.EngineerModel.objects.get(id=id).delete()
            if elecdel:
                return Response({'msg':'数据删除成功'})
            else:
                return Response({'msg':'数据删除失败!'})
        except models.EngineerModel.DoesNotExist:
            raise NotFound(detail='要删除的数据不存在!')
        
        
# 该视图接口仅用于查找单条数据
class EngiSelectView(APIView):
    def get(self, request, id): # 根据ID查找单条数据
        # 根据ID查找对应数据
        selectdata = models.EngineerModel.objects.get(id=id)
        # 序列化查找到的数据
        # many=True 参数仅在序列化查询集（即多个对象）时使用
        ser = serializers.EngiSerializer(instance=selectdata)
        # 返回序列化后的数据
        return Response(ser.data, status=200)