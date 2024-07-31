from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.ShowView.as_view()),
    path('add/', views.AddView.as_view()),
    path('edit/<int:id>', views.EditView.as_view()),
    path('del/<int:id>', views.DelView.as_view()),
]
