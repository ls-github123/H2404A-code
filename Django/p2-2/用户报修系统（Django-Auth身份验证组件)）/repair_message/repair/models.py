from django.db import models
# (User) Django 自带的用户模型，包含了用户名、密码、电子邮件等基本信息
from django.contrib.auth.models import User 

# 扩展Django-User模型信息 增加性别、爱好等
class UserProfile(models.Model):
    # OneToOneField, 与 User 模型一对一关联，表示每个用户有且只有一个 UserProfile 实例。
    # on_delete=models.CASCADE 表示当 User 被删除时,相关的 UserProfile 也会被删除
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    gender = models.CharField('性别', max_length=5, null=False)
    hobby = models.CharField('爱好', max_length=50, null=True, blank=True)
    address = models.CharField('所在城市', max_length=50, null=False)
    intro = models.TextField('用户信息简介(备注)', null=True, blank=True)
    
    class Meta:
        db_table = 'user_profile'
        managed = True
        verbose_name = '用户基本信息'
        verbose_name_plural = '用户基本信息'
    
    def __str__(self):
        # username字段包含在Django-User用户模型中
        return self.user.username

# 存储维修单信息
class Upkeep(models.Model):
    title = models.CharField('报修项目', max_length=50, null=False)
    content = models.TextField('项目详情')
    worker = models.CharField('维修人', max_length=50, null=False)
    createtime = models.DateTimeField('报修时间', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='报修用户')
    
    class Meta:
        db_table = 'upkeep'
        managed = True
        verbose_name = '报修信息'
        verbose_name_plural = '报修信息'
        
    def __str__(self):
        return self.title