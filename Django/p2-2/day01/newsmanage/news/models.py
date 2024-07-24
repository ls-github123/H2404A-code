from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category = models.CharField('类别', max_length=10, unique=True, null=False)
    
    class Meta:
        db_table = 'news_category'
        managed = True
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'
        
    def __str__(self):
        return self.category


class NewsItem(models.Model):
    title = models.CharField('新闻标题', max_length=50, null=False, unique=True)
    author = models.CharField('作者', max_length=20, null=False)
    category = models.ForeignKey(NewsCategory, related_name='news_items', on_delete=models.CASCADE, verbose_name='新闻类别')
    content = models.TextField('新闻内容')
    create_time = models.DateTimeField('发布时间', auto_now_add=True, null=False)
    update_time = models.DateTimeField('修改时间', auto_now=True, null=True)
    
    class Meta:
        db_table = 'news_item'
        managed = True
        verbose_name = '新闻条目'
        verbose_name_plural = '新闻条目'
        
    def __str__(self):
        return self.title