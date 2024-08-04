from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Index.as_view()),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('check/', views.Check.as_view()),
    path('add/', views.Addmessage.as_view())
]