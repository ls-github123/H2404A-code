from django.contrib import admin
from . import models
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookname', 'author', 'publish', 'createtime', 'price', 'num', 'sale', 'sell', 'cover', 'data_createtime', 'data_updatetime')
    search_fields = ('id', 'bookname', 'author', 'publish', 'createtime', 'price', 'num')
    list_filter = ('author', 'publish', 'createtime', 'sell')
    ordering = ('-createtime',)
    
admin.site.register(models.BooksInfo, BookInfoAdmin)