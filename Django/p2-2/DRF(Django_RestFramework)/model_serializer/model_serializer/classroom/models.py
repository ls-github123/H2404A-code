from django.db import models

# Create your models here.
class ClassModel(models.Model):
    roomname = models.CharField('教室命名', max_length=20, null=False)
    roomuse = models.CharField('教室用途', max_length=50, null=False)
    roomdesc = models.CharField('教室说明', max_length=100, null=True, blank=True)
    createtime = models.DateTimeField('记录创建时间', auto_now_add=True)
    updatetime = models.DateTimeField('记录修改时间', auto_now=True)
    
    class Meta:
        db_table = 'classroom_info'
        managed = True
        verbose_name = '教室信息'
        verbose_name_plural = '教室信息'
        
    def __str__(self):
        return self.roomname