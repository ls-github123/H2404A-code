from django.contrib import admin
from . import models
# Register your models here.
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'content', 'create_time', 'update_time')
    search_fields = ('id', 'title', 'author') # 搜索框
    list_filter = ('category', 'author', 'create_time') # 右侧过滤器
    ordering = ('-create_time',) # 默认排序
    
admin.site.register(models.NewsCategory, NewsCategoryAdmin)
admin.site.register(models.NewsItem, NewsItemAdmin)