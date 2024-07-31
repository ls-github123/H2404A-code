from django.contrib import admin
from . import models
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'brand_info')
    list_filter = ('brand_name',)

admin.site.register(models.Brand, BrandAdmin)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_name', 'goods_brand', 'goods_price', 'goods_number', 'goods_info', 'shelf_time', 'create_time', 'update_time')
    search_fields = ('id', 'goods_name', 'goods_brand', 'goods_number', 'goods_price')
    list_filter = ('goods_brand', 'shelf_time', 'create_time', 'update_time')
    
admin.site.register(models.Goods, GoodsAdmin)