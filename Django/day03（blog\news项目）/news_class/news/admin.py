from django.contrib import admin
from .models import News
# Register your models here.
class Newsadmin(admin.ModelAdmin):
    list_display = ('title','publication_date','views','likes')
    
admin.site.register(News,Newsadmin)