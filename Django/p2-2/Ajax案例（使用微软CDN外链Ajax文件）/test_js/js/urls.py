from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('list/', views.User.as_view()),
    path('test_ajax/', views.show),
    path('data/', views.Member.as_view()),
    path('del_data/', views.DelUser.as_view()),
]
