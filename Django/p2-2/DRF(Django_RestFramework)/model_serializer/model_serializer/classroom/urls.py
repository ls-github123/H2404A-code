from django.urls import path
from . import views

urlpatterns = [
    path('clsshow/', views.ClassRoomView.as_view()),
]
