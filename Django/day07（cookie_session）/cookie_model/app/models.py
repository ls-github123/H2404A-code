from django.db import models
# make_password 加密明文密码 \ check_password 用于校验密码哈希
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.

# 创建用户user模型
class UserModel(models.Model):
    user_name = models.CharField(max_length=20, unique=True, null=True, verbose_name='用户名')
    user_mobile = models.CharField(max_length=15, unique=True, null=True, verbose_name='手机号')
    user_pwd = models.CharField(max_length=128, null=True, verbose_name='密码(自动哈希加密)')
    
    # 将用户的原始密码（raw_password）进行哈希加密，并将加密后的密码存储在数据库中
    def set_password(self, raw_password):
        # Django内置的函数 make_password(raw_password) 用于将原始密码进行哈希加密
        # 包含用于验证的盐(salt)
        # self.user_pwd 将加密后的值赋值给user_pwd字段
        self.user_pwd = make_password(raw_password) 
        self.save() # 将哈希加密后的用户密码写入数据库
    
    # 验证用户输入的原始密码（raw_password）是否与存储在数据库中的加密密码相匹配
    def check_password(self, raw_password):
        return check_password(raw_password, self.user_pwd)
    
    def save(self, *args, **kwargs):
        if not self.user_pwd.startswith('pbkdf2_'):  # 检查密码是否已经加密
            self.set_password(self.user_pwd)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'user_model'
        managed = True
        verbose_name = '用户账户信息'
        verbose_name_plural = '用户账户信息'
    
    def __str__(self):
        return self.user_name

# 创建新闻News模型
class NewsModel(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='新闻标题')
    content = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='作者')
    
    class Meta:
        db_table = 'news_model'
        managed = True
        verbose_name = '新闻条目'
        verbose_name_plural = '新闻条目'
    
    def __str__(self):
        return self.title
    