from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title = models.CharField('新闻标题', max_length=50, null=False)
    content = models.CharField('新闻内容', max_length=100, null=True, blank=True)
    createtime = models.DateTimeField('发布时间', auto_now_add=True)
    
    class Meta:
        db_table = 'news_model'
        managed = True
        verbose_name = '新闻条目'
        verbose_name_plural = '新闻条目'
        
    def __str__(self):
        return self.title