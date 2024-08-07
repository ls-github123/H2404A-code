from django.db import models

# Create your models here.
class EngineerModel(models.Model):
    name = models.CharField('工程师姓名', max_length=20, null=False)
    age = models.IntegerField('年龄', null=False)
    professional = models.CharField('专业', max_length=10, null=False)
    descinfo = models.CharField('个人简介', max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'engineer_info'
        managed = True
        verbose_name = '工程师信息'
        verbose_name_plural = '工程师信息'
        
    def __str__(self):
        return self.name