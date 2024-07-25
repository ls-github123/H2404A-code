from django.contrib import admin
from . import models
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'number', 'category')
    search_fields = ('id', 'name', 'number', 'category')
    list_filter = ('category',)
    
admin.site.register(models.GoodsInfo, GoodsInfoAdmin)