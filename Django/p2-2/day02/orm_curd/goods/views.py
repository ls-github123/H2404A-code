from django.shortcuts import render, HttpResponseRedirect
from . import models

def show(request):
    if 'select' in request.GET:
        select = request.GET['select']
        data = models.GoodsInfo.objects.filter(price=select)
        print(data)
    else:
        data = models.GoodsInfo.objects.all()
    return render(request, 'goods/list.html', {'data':data})

def add(request):
    if request.method == 'POST':
        goodsinfo = models.GoodsInfo.objects.create(
            name = request.POST['goods_name'],
            price = request.POST['goods_price'],
            number = request.POST['goods_number'],
            category = request.POST['goods_category']
        )
        if goodsinfo:
            return HttpResponseRedirect('/goods/show')
    else:
        return render(request, 'goods/add.html')
    
def deldata(request):
    pk = request.GET['id']
    res = models.GoodsInfo.objects.filter(id=pk).delete()
    if res:
        return HttpResponseRedirect('goods/show')