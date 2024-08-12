from django.db import models
from django.core.validators import MinValueValidator # 整数字段验证器


class ComputerModel(models.Model):
    name = models.CharField('计算机型号', max_length=20, null=False)
    price = models.DecimalField('零售价格', max_digits=7, decimal_places=2, null=False)
    number = models.IntegerField('库存数量', validators=[MinValueValidator(0)], null=False)
    detail = models.TextField('产品详情')
    
    class Meta:
        db_table = 'computer_info'
        managed = True
        verbose_name = '计算机库存信息'
        verbose_name_plural = '计算机库存信息'
        
    def __str__(self):
        return self.name