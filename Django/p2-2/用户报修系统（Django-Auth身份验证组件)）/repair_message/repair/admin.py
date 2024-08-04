from django.contrib import admin
from . import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'hobby', 'address', 'intro')
    list_filter = ('gender',)
    
admin.site.register(models.UserProfile, UserProfileAdmin)

class UpkeepAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'worker', 'createtime', 'user')
    search_fields = ('id', 'title', 'worker', 'createtime')
    list_filter = ('worker', 'createtime')
    
admin.site.register(models.Upkeep, UpkeepAdmin)