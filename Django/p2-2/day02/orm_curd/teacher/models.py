from django.db import models

# Create your models here.
class TeachersInfo(models.Model):
    gender_choices = (
        ('男','男'),
        ('女','女')
    )
    
    name = models.CharField('教师姓名', max_length=20, null=False)
    gender = models.CharField('性别', max_length=2, choices=gender_choices, null=False)
    age = models.IntegerField('年龄',)
    course = models.CharField('任教科目', max_length=15, null=False)
    salary = models.DecimalField('薪资', max_digits=7, decimal_places=2, null=False)
    address = models.TextField('居住地址')
    onboarding_time = models.DateTimeField('入职时间',null=False)
    personal_info = models.TextField('备注信息(选填)', null=True)
    create_time = models.DateTimeField('数据添加时间', auto_now_add=True)
    update_time = models.DateTimeField('数据修改时间',auto_now=True)
    
    class Meta:
        db_table = 'teachers_info'
        managed = True
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'
        
    def __str__(self):
        return self.name