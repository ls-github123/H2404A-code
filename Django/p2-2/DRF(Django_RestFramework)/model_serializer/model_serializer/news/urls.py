from django.urls import path
from 。 import views

urlpatterns = [
    path('list/', views.NewsList.as_view()),
    path('add/', views.NewsList.as_view()),
    path('update/<int:id>/', views.NewsList.as_view()),
    path('del/<int:pk>/', views.NewsList.as_view()),
]
