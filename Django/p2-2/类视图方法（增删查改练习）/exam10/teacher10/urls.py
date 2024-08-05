from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.ShowView.as_view(), name='show'),
    path('add/', views.AddInfoView.as_view(), name='add'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit'),
    path('del/<int:id>/', views.DeleteView.as_view(), name='del'),
]
