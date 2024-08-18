from django.db import models

# 留言分类
class MesCateModel(models.Model):
    name = models.CharField('分类名称', max_length=20, null=False)
    intro = models.CharField('分类描述', max_length=50)
    
    class Meta:
        db_table = 'mescate'
        managed = True
        verbose_name = '留言分类'
        verbose_name_plural = '留言分类'
        
    def __str__(self):
        return self.name
    
# 留言内容
class MessageModel(models.Model):
    title = models.CharField('留言标题', max_length=20, null=False)
    author = models.CharField('留言人', max_length=20, null=False)
    content = models.TextField('留言内容')
    cate = models.ForeignKey(MesCateModel, on_delete=models.CASCADE, db_column='cate', verbose_name='留言类型')
    
    class Meta:
        db_table = 'messagemodel'
        managed = True
        verbose_name = '留言内容'
        verbose_name_plural = '留言内容'
        
    def __str__(self):
        return self.title