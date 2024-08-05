from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    tname = models.CharField('教师姓名', max_length=10, null=False)
    tclass = models.CharField('教授课程', max_length=10, null=False)
    tdesc = models.TextField('个人简介', null=True, blank=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True)
    updatetime = models.DateTimeField('更新时间', auto_now=True)
    
    class Meta:
        db_table = 'teacher_info'
        managed = True
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'
        
    def __str__(self):
        return self.tname
