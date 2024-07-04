from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('news/', views.news_list, name='news_list'),
]
