from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', views.TaskView)

# 路由挂载
urlpatterns = [
    path('', include(router.urls)),
]
