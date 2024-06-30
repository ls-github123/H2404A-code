from django.urls import path
from . import views

urlpatterns = [
    path('add_user/',views.add_user,name='add_user'),
    path('add_blog/', views.add_blog,name='add_blog'),
    path('recent_blogs/<int:user_id>/', views.recent_blogs, name='recent_blogs'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
]
