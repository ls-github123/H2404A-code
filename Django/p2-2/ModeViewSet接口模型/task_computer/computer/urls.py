from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('com', views.ComputerView)

# 路由挂载
urlpatterns = [
    path('', include(router.urls)),
]