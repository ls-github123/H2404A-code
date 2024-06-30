from django.db import models

# Create your models here.
class Userprofile(models.Model):
    username = models.CharField(max_length=10,verbose_name='用户名')
    age = models.IntegerField(verbose_name='用户年龄')
    height = models.FloatField(verbose_name='用户身高')
    
    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'
    def __str__(self):
        return self.username

class Blogdata(models.Model):
    # 外键字段，指向Userprofile模型，当删除一个作者时
    # on_delete=models.CASCADE参数将确保所有关联的博客也会被删除
    author = models.ForeignKey(Userprofile, on_delete=models.CASCADE, verbose_name='作者',related_name='blogs')
    title = models.CharField(max_length=20, verbose_name='博客标题')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    content = models.TextField(verbose_name='博客内容')
    
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
    
    def __str__(self):
        return self.title
    