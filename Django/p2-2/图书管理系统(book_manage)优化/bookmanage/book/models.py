from django.db import models
from django.core.validators import MinValueValidator # 整数字段验证器

class BooksInfo(models.Model):
    bookname = models.CharField('书名', max_length=20, null=False)
    author = models.CharField('作者', max_length=20, null=False)
    publish = models.CharField('出版社', max_length=30, null=False)
    createtime = models.DateField('出版时间', null=False)
    price = models.DecimalField('零售价格', max_digits=6, decimal_places=2, null=False)
    num = models.IntegerField('库存数量', default=0, validators=[MinValueValidator(0)], null=False)
    sale = models.IntegerField('销售数量', default=0, validators=[MinValueValidator(0)], null=False)
    sell = models.BooleanField('是否上架', default=False)
    cover = models.ImageField(default='https://static.djangoproject.com/img/logos/django-logo-negative.png', verbose_name='封面图片路径')
    data_createtime = models.DateTimeField('数据添加时间', auto_now_add=True)
    data_updatetime = models.DateTimeField('数据修改时间', auto_now=True)
    
    class Meta:
        db_table = 'book_info'
        managed = True
        verbose_name = '书籍信息'
        verbose_name_plural = '书籍信息'
        
    def __str__(self):
        return self.bookname