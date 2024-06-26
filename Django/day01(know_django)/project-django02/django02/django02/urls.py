"""
URL configuration for django02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django02.views import books, title, shop, cdn
from django02.views import book, index1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books),
    path('title/', title),
    path('shop/', shop),
    path('cdn/', cdn),
    path('book/', book),
    path('index/', index1)
]
