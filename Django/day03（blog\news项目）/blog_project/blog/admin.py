from django.contrib import admin
from .models import Userprofile, Blogdata
# Register your models here.
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('username','age','height',)
    list_display_links = ('username',)
    search_fields = ('username',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date',)
    list_display_links = ('title',)
    search_fields = ('title', 'author__username',)

admin.site.register(Userprofile, UserprofileAdmin)
admin.site.register(Blogdata, BlogAdmin)