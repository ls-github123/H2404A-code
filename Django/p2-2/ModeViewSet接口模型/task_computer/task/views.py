from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet # modelviewset 模型视图类
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

class TaskView(ModelViewSet):
    # 设置查询集
    queryset = models.TaskModel.objects.all()
    # 定义序列化类
    serializer_class = serializers.TaskSerializers
    # 定义分页类
    pagination_class = Pagination
    
    # 设置过滤及排序
    # filters.OrderingFilter 过滤器允许用户在请求中指定排序参数，从而动态地对查询集进行排序
    # 用户可以通过 URL 参数 ordering 来指定排序字段
    # 例如：?ordering=createtime 将按照创建时间进行升序排序
    
    # filters.SearchFilter 过滤器允许用户通过指定的字段进行搜索
    # 用户可以通过 URL 参数 search 来进行搜索
    # 例如：?search=User A
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    
    # 设置搜索字段
    search_fields = ['title', 'publish']
    # 设置默认排序字段
    ordering_fields = ['createtime']
    
    # Postman 使用 GET 请求访问 /tasks/，并在 URL 中添加搜索和分页参数即可
    # 分页: http://<your-domain>/task/?page=2&size=5
    # 搜索: http://<your-domain>/task/?search=User A
    # 分页后的搜索: http://<your-domain>/tasks/?search=User A&page=1&size=5
    # 这些操作将允许你搜索特定发布人或标题，并在搜索结果中进行分页
    
    # 查询所有数据并分页
    def list(self, request, *args, **kwargs):
        # 获取经过过滤后的查询集
        queryset = self.filter_queryset(self.get_queryset())
        # 对过滤后的查询集进行分页
        page = self.paginate_queryset(queryset)
        
        if page is not None: #如果 page 不为 None 则分页成功
            # 处理分页后的响应
            # 将分页后的数据序列化
            ser = self.get_serializer(page, many=True)
            # 返回分页后的响应，并添加状态信息和消息
            return self.get_paginated_response({
                "status":200,
                "msg":"OK",
                "results":ser.data
            })
        # page 为 None 没有分页或参数错误 分页失败
        # 处理完整数据集的响应
        # 对完整的查询集进行序列化
        ser = self.get_serializer(queryset, many=True)
        return Response({
            "status":200,
            "msg":"OK",
            "results":ser.data
        })
    
    # 添加数据
    def create(self, request, *args, **kwargs):
        # super().create() 的返回值通常是一个包含新创建对象数据的 Response 对象
        response = super().create(request, *args, **kwargs)
        return Response({
            "status":200,
            "msg":"数据添加成功",
            "data":response.data
        })
        
    # 修改编辑数据
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "status":200,
            "msg":"数据编辑成功",
            "data":response.data
        })
    
    # 删除数据
    def destroy(self, request, *args, **kwargs):
        # 调用父类 destroy()方法执行删除逻辑 没有返回数据
        super().destroy(request, *args, **kwargs)
        return Response({
            "status":204,
            "msg":"数据删除成功",
            "data":None
        })