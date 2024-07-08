from django.shortcuts import render, redirect
# authenticate用于验证给定的用户名和密码是否匹配现有用户
# login 用于将用户标记为已登录,通常在用户通过身份验证后调用
# logout 用于将用户标记为已注销，清除用户会话数据
from django.contrib.auth import authenticate, login, logout

# User Django内置的用户模型，用于管理用户数据(如用户名、密码、电子邮件等)
# 用于创建新用户及查询用户信息
from django.contrib.auth.models import User 

# login_required 一个装饰器,用于限制某些视图只能被已登录的用户访问
# (如用户未登录，则会重定向到登录页面)
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm
# Create your views here.

def register(request): # 用户注册模块
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') # 验证通过，重定向到登录界面login
    return render(request, 'shop/register.html') # 如果使用get方法请求，则打开注册页面register

def login_view(request): # 用户登录模块
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
    return render(request, 'shop/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products':products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form':form})