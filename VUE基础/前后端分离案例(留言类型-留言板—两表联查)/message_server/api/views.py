from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from . import models
from . import serializers

# 定义分页类
class Pagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 5
    
class CateView(ModelViewSet):
    queryset = models.MesCateModel.objects.all()
    serializer_class = serializers.CateSerializer
    
class MessageView(ModelViewSet):
    queryset = models.MessageModel.objects.all()
    serializer_class = serializers.MessageSerializer
    pagination_class = Pagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    
    search_fields = ['title', 'author']
    ordering_fields = ['id']
    
    # 查询所有数据并分页
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "status":200,
                "message":"OK",
                "results":ser.data
            })
        ser = self.get_serializer(queryset, many=True)
        return Response({
            "status":200,
            "message":"OK",
            "results":ser.data
        })
    
    # 重写create方法
    def create(self, request, *args, **kwargs):
        self.serializer_class = serializers.MessageAddSerializer
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status":200, "data":ser.data})
        else:
            return Response({"status":400, "data":ser.errors})
        
    # 重写update方法
    def update(self, request, *args, **kwargs):
        self.serializer_class = serializers.MessageAddSerializer
        info = self.queryset.get(pk=kwargs.get('pk'))
        ser = self.serializer_class(instance=info, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status":200, "data":ser.data})
        else:
            return Response({"status":400, "data":ser.errors})
        
    # 删除数据
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            "status":204,
            "message":"数据删除成功",
            "data":None
        })