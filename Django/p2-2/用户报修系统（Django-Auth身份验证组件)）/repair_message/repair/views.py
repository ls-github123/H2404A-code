# get_object_or_404获取对象，如对象不存在则返回404错误
# redirect重定向到指定URL
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
# authenticate\login\logout 处理用户身份验证、登录和注销操作
from django.contrib.auth import authenticate, login, logout
# 引入Django自带的用户模型 User
from django.contrib.auth.models import User
# LoginRequiredMixin 确保用户登录后才能访问的混合类
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from . import models

# 用户注册视图模块
class RegisterView(View):
    def get(self, request):
        return render(request, 'repair/register.html')
    
    def post(self, request):
        # username\password\email 字段包含在Django-User模型中
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        hobby = request.POST.get('hobby')
        address = request.POST.get('address')
        intro = request.POST.get('intro')
        
        user = User.objects.create_user(
            username=username, 
            password=password,
            email=email,
        )
        
        userprofile = models.UserProfile.objects.create(
            user=user, 
            gender=gender, 
            hobby=hobby, 
            address=address,
            intro=intro 
        )
        
        if userprofile:
            return redirect('login') # 注册成功后重定向到登录页面
        else:
            return HttpResponse('注册用户失败!') # 如注册失败 则返回失败提示
        
# 用户登录视图模块
class LoginView(View):
    def get(self, request):
        return render(request, 'repair/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user 认证用户
        user = authenticate(request, username=username, password=password)
        
        if user is not None: # 如果用户存在且验证通过
            login(request, user) # login()方法 登录用户
            return redirect('home')
        else: # 用户验证失败
            # 返回渲染登录页面 并显示错误信息
            return render(request, 'repair/login.html', {'error':'Invalid credentials'})

# 用户登录注销视图模块
class LogoutView(View):
    def get(self, request):
        logout(request) # logout()方法 注销用户
        return redirect('login') # 返回登录页面

# 主页视图模块，显示用户的报修信息列表
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取当前用户的所有维修单
        upkeeps = models.Upkeep.objects.filter(user=request.user)
        return render(request, 'repair/home.html', {'upkeeps':upkeeps})

# 添加报修单视图模块
# 只有登录用户才能访问添加
class AddUpkeepView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'repair/add_upkeep.html')
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        worker = request.POST.get('worker')
        upkeep = models.Upkeep.objects.create(
            title=title,
            content=content,
            worker=worker,
            user=request.user,
        )
        if upkeep:
            return redirect('home') # 添加成功后重定向到主页
        
# 编辑报修单视图模块
# LoginRequiredMixin 只有登录用户才能访问
class EditUpkeepView(LoginRequiredMixin, View):
    def get(self, request, upkeep_id):
        upkeep = get_object_or_404(models.Upkeep, id=upkeep_id, user=request.user)
        return render(request, 'repair/edit_upkeep.html', {'upkeep':upkeep})
    
    def post(self, request, upkeep_id):
        upkeep = get_object_or_404(models.Upkeep, id=upkeep_id, user=request.user)
        upkeep.title = request.POST.get('title')
        upkeep.content = request.POST.get('content')
        upkeep.worker = request.POST.get('worker')
        upkeep.save()
        return redirect('home')
    
# 删除维修单视图模块
class DeleteUpkeepView(LoginRequiredMixin, View):
    def post(self, request, upkeep_id):
        upkeep = get_object_or_404(models.Upkeep, id=upkeep_id, user=request.user)
        upkeep.delete()
        return redirect('home')
    
# 查看维修单详情视图模块
class UpkeepDetaView(LoginRequiredMixin, View):
    def get(self, request, upkeep_id):
        upkeep = get_object_or_404(models.Upkeep, id=upkeep_id, user=request.user)
        return render(request, 'repair/upkeep_detail.html', {'upkeep':upkeep})