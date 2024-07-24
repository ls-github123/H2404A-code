from django.contrib import admin
from .models import StudentInfo
# Register your models here.

class StuinfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'introduce', 'class_name', 'create_time']
    
admin.site.register(StudentInfo, StuinfoAdmin)