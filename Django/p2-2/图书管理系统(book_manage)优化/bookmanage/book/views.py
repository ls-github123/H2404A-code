from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.db.models import Q

# 图书信息展示
def show(request):
    if request.method == 'POST':
        # 从 POST 数据中获取 select 字段，并去掉前后的空格
        # 如果字段不存在，返回空字符串
        select = request.POST.get('select', '').strip() 
        sell = request.POST.get('sell') # 同上
        filters = Q() # 初始化过滤器
        if select:
            filters &= Q(bookname__contains=select)
        if sell is not None:
            filters &= Q(sell=sell)
        data = models.BooksInfo.objects.filter(filters)
    
    else:
        data = models.BooksInfo.objects.all()
    
    return render(request, 'book/show.html', {'data':data})

# 图书信息添加
def add(request):
    if request.method == 'POST':
        book_info = models.BooksInfo.objects.create(
            bookname = request.POST['book_name'],
            author = request.POST['book_author'],
            publish = request.POST['book_publish'],
            createtime = request.POST['book_createtime'],
            price = request.POST['book_price'],
            num = request.POST['book_num'],
            sale = request.POST['book_sale'],
            sell = request.POST['book_sell'],
            cover = request.POST['book_cover']
        )
        if book_info:
            return HttpResponseRedirect('/book/')
        else:
            return HttpResponse('数据添加失败!', stutus=400)
    else:
        return render(request, 'book/add.html')

# 图书信息选择编辑
def edit(request):
    if request.method == 'GET':
        bookinfo = models.BooksInfo.objects.get(id=request.GET['id'])
        return render(request, 'book/edit.html', {'bookinfo':bookinfo})
    
    if request.method == 'POST':
        result = models.BooksInfo.objects.get(id=request.POST['book_id'])
        result.bookname = request.POST['book_name']
        result.author = request.POST['book_author']
        result.publish = request.POST['book_publish']
        result.createtime = request.POST['book_createtime']
        result.price = request.POST['book_price']
        result.num = request.POST['book_num']
        result.sale = request.POST['book_sale']
        result.sell = request.POST['book_sell']
        result.cover = request.POST['book_cover']
        # 使用.save()方法提交数据 
        # 以触发模型中data_updatetime字段的add_now自动更新
        result.save() 
        return redirect('/book/')
        

def deldata(request):
    pk = request.GET['id']
    res = models.BooksInfo.objects.filter(id=pk).delete()
    
    if res[0]: # 检查删除的记录数是否大于0
        return HttpResponseRedirect('/book/')
    else:
        return HttpResponse('删除失败!', status=400)