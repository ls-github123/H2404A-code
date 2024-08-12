from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet # modelviewset 组件
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination # 分页组件
from rest_framework import filters
from . import models
from . import serializers

# 定义分页类
class Pagination(PageNumberPagination):
    page_query_param = 'page' # 定义页码参数名
    page_size_query_param = 'size' # 定义每页显示数量参数名
    page_size = 5 # 默认每页显示5条数据
    
    
class ComputerView(ModelViewSet):
    queryset = models.ComputerModel.objects.all()
    # 定义序列化类
    serializer_class = serializers.ComputerSerializers
    # 定义分页类
    pagination_class = Pagination
    
    # 设置过滤及排序
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    
    # 设置搜索字段
    # 使用型号(name)或价格(price)进行搜索
    search_fields = ['name', 'price']
    
    # 设置默认排序字段
    ordering_fields = ['number']
    
    # 查询所有数据并分页
    def list(self, request, *args, **kwargs):
        # 获取经过滤后的查询集
        queryset = self.filter_queryset(self.get_queryset())
        # 对过滤后的查询集进行分页
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "status":200,
                "msg":"OK",
                "results":ser.data
            })
        ser = self.get_serializer(queryset, many=True)
        return Response({
            "status":200,
            "msg":"OK",
            "results":ser.data
        })
        
    # 添加数据
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "status":200,
            "msg":"数据提交成功",
            "data":response.data
        })
        
    # 修改编辑数据
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "status":200,
            "msg":"数据修改成功",
            "data":response.data
        })
        
    # 删除数据
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            "status":204,
            "msg":"数据删除成功",
            "data":None
        })