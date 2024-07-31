from django.db import models
from django.core.validators import MinValueValidator # 整数字段验证器

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField('品牌名称', max_length=20, null=False, unique=True)
    brand_info = models.TextField('品牌简介', null=True, blank=True)
    
    class Meta:
        db_table = 'brand_info'
        managed = True
        verbose_name = '品牌信息'
        verbose_name_plural = '品牌信息'
        
    def __str__(self):
        return self.brand_name
    
class Goods(models.Model):
    goods_name = models.CharField('商品名称', max_length=20, null=False, unique=True)
    goods_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column='goods_brand', verbose_name='所属品牌')
    goods_price = models.DecimalField('商品价格', max_digits=7, decimal_places=2, null=False)
    goods_number = models.IntegerField('库存数量', default=0, validators=[MinValueValidator(0)], null=False)
    goods_info = models.TextField('商品详情', null=True, blank=True)
    shelf_time = models.DateField('上架时间', null=False)
    create_time = models.DateTimeField('数据添加时间', auto_now_add=True)
    update_time = models.DateTimeField('数据修改时间', auto_now=True)
    
    class Meta:
        db_table = 'goods_info'
        managed = True
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
    
    def __str__(self):
        return self.goods_name