from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField('任务主题', max_length=30, null=False)
    publish = models.CharField('发布人', max_length=20, null=False)
    desc = models.TextField('任务详情')
    createtime = models.DateTimeField('发布时间', auto_now_add=True)
    
    class Meta:
        db_table = 'task_model'
        managed = True
        verbose_name = '任务信息'
        verbose_name_plural = '任务信息'
        
    def __str__(self):
        return self.title