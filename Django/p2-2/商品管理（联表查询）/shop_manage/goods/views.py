from django.shortcuts import render, get_object_or_404
from django.views import View
from . import models
from django.http import HttpResponse, HttpResponseRedirect

# 商品信息展示
class ShowView(View):
    def get(self, request):
        brand = models.Brand.objects.all()
        goods = []
        for info in brand:
            goods.extend(info.goods_set.all())
        return render(request, 'goods/show.html', {'goods':goods})
    
    def post(self, request):
        keyword = request.POST.get('goods_select', '')
        goods = models.Goods.objects.filter(goods_name__icontains=keyword)
        return render(request, 'goods/show.html', {'goods':goods})
    
# 商品信息添加
class AddView(View):
    def get(self, request):
        brand = models.Brand.objects.all()
        return render(request, 'goods/add.html', {'brand':brand})
    
    def post(self, request):
        # 需要在创建 Goods 实例之前先获取 Brand 实例，并确保代码中的逗号和缩进正确
        brand_id = request.POST.get('goods_brand')
        brand = get_object_or_404(models.Brand, id=brand_id)
        goods_data = models.Goods.objects.create(
            goods_name = request.POST['goods_name'],
            goods_brand = brand,
            goods_price = request.POST['goods_price'],
            goods_number = request.POST['goods_number'],
            goods_info = request.POST['goods_info'],
            shelf_time = request.POST['shelf_time']
        )
        if goods_data:
            return HttpResponseRedirect('/goods/show')
        else:
            return HttpResponse('商品信息添加失败!', status=400)
        
# 商品信息编辑
class EditView(View):
    def get(self, request, id):
        goods = get_object_or_404(models.Goods, id=id)
        brands = models.Brand.objects.all()
        return render(request, 'goods/edit.html', {'goods':goods, 'brands':brands})
    
    def post(self, request, id):
        result = get_object_or_404(models.Goods, id=id)
        result.goods_name = request.POST['goods_name']
        # 需要先获取相应的 Brand 实例，然后将其分配给 result.goods_brand
        brand_id = request.POST.get('goods_brand')
        result.goods_brand = get_object_or_404(models.Brand, id=brand_id)
        result.goods_price = request.POST['goods_price']
        result.goods_number = request.POST['goods_number']
        result.goods_info = request.POST['goods_info']
        result.shelf_time = request.POST['shelf_time']
        # 使用.save()方法提交数据 
        # 以触发模型中update_time字段的add_now自动更新
        result.save()
        return HttpResponseRedirect('/goods/show')
    
    
# 商品信息删除
class DelView(View):
    def get(self, request, id):
        res = models.Goods.objects.filter(id=id).delete()
        if res[0]:
            return HttpResponseRedirect('/goods/show')
        else:
            return HttpResponse('商品信息删除失败!', status=400)