from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel, NewsModel
from .forms import LoginForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserModel.objects.get(user_name=username)
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    return redirect('news_list')
                else:
                    return HttpResponse('密码错误!')
            except UserModel.DoesNotExist:
                return HttpResponse('用户不存在')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def news_list(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = UserModel.objects.get(id=user_id)
            news_list = NewsModel.objects.all()
            return render(request, 'news_list.html', {'news_list':news_list})
        except UserModel.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')