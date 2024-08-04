from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'), # 用户注册
    path('login/', views.LoginView.as_view(), name='login'), # 用户登录
    path('logout/', views.LogoutView.as_view(), name='logout'), # 用户注销登录
    path('', views.HomeView.as_view(), name='home'), # 主页视图
    path('add/', views.AddUpkeepView.as_view(), name='add_upkeep'), # 添加报修单
    path('edit/<int:upkeep_id>/', views.EditUpkeepView.as_view(), name='edit_upkeep'), # 编辑报修单
    path('delete/<int:upkeep_id>/', views.DeleteUpkeepView.as_view(), name='delete_upkeep'), # 删除报修单
    path('detail/<int:upkeep_id>/', views.UpkeepDetaView.as_view(), name='detail_upkeep'), # 查看报修单详情
]
