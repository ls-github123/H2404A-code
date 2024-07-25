from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show),
    path('add/', views.add),
    path('del/', views.deldata),
]
