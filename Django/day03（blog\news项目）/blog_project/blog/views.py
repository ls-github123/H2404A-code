# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Userprofile, Blogdata

def add_user(request):
    # 添加用户数据的视图函数
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        height = request.POST.get('height')
        user = Userprofile(username=username, age=age, height=height)
        user.save()
        return JsonResponse({'status': 'User added'})
    return render(request, 'blog/add_user.html')

def add_blog(request):
    # 添加博客数据的视图函数
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = get_object_or_404(Userprofile, id=author_id)
        blog = Blogdata(author=author, title=title, content=content)
        blog.save()
        return JsonResponse({'status': 'Blog added'})
    return render(request, 'blog/add_blog.html')

def recent_blogs(request, user_id):
    # 查询某用户最近发布的5篇博客文章
    user = get_object_or_404(Userprofile, id=user_id)
    blogs = Blogdata.objects.filter(author=user).order_by('-published_date')[:5]
    return render(request, 'blog/recent_blogs.html', {'user': user, 'blogs': blogs})

def delete_blog(request, blog_id):
    # 删除博客文章的视图函数
    blog = get_object_or_404(Blogdata, id=blog_id)
    blog.delete()
    return redirect('recent_blogs', user_id=blog.author.id)
