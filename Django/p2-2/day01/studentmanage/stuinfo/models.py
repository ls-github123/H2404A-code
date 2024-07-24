from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField('学生姓名', max_length=20, null=False)
    gender = models.CharField('性别', max_length=1, null=False)
    age = models.IntegerField('年龄', null=False)
    introduce = models.TextField('自我介绍')
    class_name = models.CharField('所属班级', max_length=5)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    
    class Meta:
        db_table = 'stu_info'
        managed = True
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
        
    def __str__(self):
        return self.name