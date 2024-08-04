from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from . import models

# 定义留言展示页
class Index(View):
    def get(self, request):
        # 获取session中的用户名信息
        username = request.session.get('username')
        # 如果为True,表示用户登录 显示该用户信息，否则显示所有信息
        if username: # 登录成功
            info = models.Message.objects.filter(mem_id=request.session.get('mid'))
        else: # 未登录或登录失败
            info = models.Message.objects.all()
        return render(request, 'message/index.html', locals())
    
# 定义注册页面
class Register(View):
    def get(self, request):
        return render(request, 'message/register.html')
    
    def post(self, request):
        # 将页面复选框回传的值转换为列表，再将列表转换为串
        hobbylist = request.POST.getlist('hobby')
        hobbystr = ','.join(hobbylist)
        res = models.Member.objects.create(
            username = request.POST['username'],
            password = request.POST['password'],
            gender = request.POST['gender'],
            hobby = hobbystr,
            intro = request.POST['intro']
        )
        if res:
            # 注册完成后返回登录页面
            return HttpResponseRedirect('/message/login')
        
# 展示登录页面视图
class Login(View):
    def get(self, request):
        return render(request, 'message/login.html')
    
    def post(self, request):
        # 获取用户输入的用户名和密码
        username = request.POST['username']
        password = request.POST['password']
        
        info = models.Member.objects.filter(username=username, password=password).values()
        infoname = models.Member.objects.filter(username=username).values()
        if info: # 登录成功 将用户名和用户ID存储到session中
            infolist = list(info)
            # 设置seesion
            request.session['mid']=infolist[0]['id'] # 添加留言时入库
            request.session['username']=infolist[0]['username'] # 在首页欢迎用户
            return HttpResponseRedirect('/message/index')
        elif infoname:
            # 登录失败但是存在用户名
            return HttpResponseRedirect('/message/login')
        else:
            # 登录失败 且不存在用户名
            return HttpResponseRedirect('/message/register')
  
class Check(View):
    def get(self, request):
        return render(request, 'message/addmessage.html')
    
# 展示添加留言表单
class Addmessage(View):
    def get(self, request):
        return render(request, 'message/addmessage.html')
    
    def post(self, request):
        mid = request.session['mid']
        if mid: # session存在用户id, 表示已登录
            res=models.Message.objects.create(
                title=request.POST['title'],
                content=request.POST['content'],
                mem=mid
            )
            if res:
                return HttpResponseRedirect('/message/index')
        else:
            # session中用户id不存在
            # 表示用户未登录, 直接跳转到登录页面
            return HttpResponseRedirect('message/login')