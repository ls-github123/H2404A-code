from django.db import models

# Create your models here.
class ElectronicModel(models.Model):
    name = models.CharField('部件名称', max_length=50, null=False)
    usability = models.CharField('可用性', max_length=4, null=False)
    specification = models.CharField('规格', max_length=50, null=False)
    createtime = models.DateField('入库时间', null=False)
    
    class Meta:
        db_table = 'electronic_info'
        managed = True
        verbose_name = '配件信息'
        verbose_name_plural = '配件信息'
        
    def __str__(self):
        return self.name