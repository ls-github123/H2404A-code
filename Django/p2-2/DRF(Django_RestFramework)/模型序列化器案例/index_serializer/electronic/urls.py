from django.urls import path
from . import views

urlpatterns = [
    path('showall/', views.ElecAllView.as_view()), # 查询展示所有数据
    path('getdata/<int:id>/', views.ElecSelectView.as_view()), # 按照ID查询单条数据
    path('add/', views.ElecAllView.as_view()), # 添加数据请求接口
    path('update/<int:id>/', views.ElecAllView.as_view()), # 修改数据请求接口
    path('del/<int:id>/', views.ElecAllView.as_view()), # 删除数据请求接口
]