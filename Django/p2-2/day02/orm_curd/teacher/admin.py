from django.contrib import admin
from . import models
# Register your models here.
class TeachersInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'age', 'course', 'salary', 'address', 'onboarding_time', 'personal_info', 'create_time', 'update_time')
    search_fields = ('id', 'name', 'gender', 'age', 'course') # 搜索框
    list_filter = ('gender', 'age', 'course', 'onboarding_time', 'create_time', 'update_time') # 右侧过滤器
    ordering = ('-onboarding_time',) # 排序方式
    
admin.site.register(models.TeachersInfo, TeachersInfoAdmin)