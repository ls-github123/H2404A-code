from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField('用户名', max_length=30, unique=True)
    password = models.CharField('密码', max_length=20)
    gender = models.CharField('性别', max_length=2, null=False)
    hobby = models.CharField('爱好', max_length=30)
    intro = models.TextField('简介')
    createtime = models.DateTimeField('注册时间', auto_now_add=True)
    
    class Meta:
        db_table = 'member'
        managed = True
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.username
    

class Message(models.Model):
    title = models.CharField('留言标题', max_length=30)
    content = models.TextField('留言内容', max_length=200)
    mem = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='发表用户')
    createtime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'message'
        managed = True
        verbose_name = '留言管理'
        verbose_name_plural = '留言管理'
        
    def __str__(self):
        return self.title