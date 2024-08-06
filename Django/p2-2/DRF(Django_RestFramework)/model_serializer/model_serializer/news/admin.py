from django.contrib import admin
from . import models
# Register your models here.
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'createtime')
    
admin.site.register(models.NewsModel, NewsModelAdmin)