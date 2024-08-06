from django.contrib import admin
from . import models
# Register your models here.
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'roomname', 'roomuse', 'roomdesc', 'createtime', 'updatetime')

admin.site.register(models.ClassModel, ClassRoomAdmin)