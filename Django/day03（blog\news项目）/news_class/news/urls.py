from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_news),
    path('update/', views.update_news),
    path('delete/', views.delete_news),
    path('query/', views.query_news),
    path('query_filtered/', views.query_news_filtered),
]