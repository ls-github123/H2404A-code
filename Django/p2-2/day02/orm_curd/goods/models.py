from django.db import models

# Create your models here.
class GoodsInfo(models.Model):
    name = models.CharField('商品名称', max_length=20, null=False)
    price = models.DecimalField('商品价格', max_digits=7, decimal_places=2, null=False)
    number = models.IntegerField('商品数量', null=False)
    category = models.CharField('商品种类',max_length=10, null=False)
    
    class Meta:
        db_table = 'goods_info'
        managed = True
        verbose_name = '教学武器商品信息'
        verbose_name_plural = '教学武器商品信息'
        
    def __str__(self):
        return self.name