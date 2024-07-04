from django.contrib import admin
from .models import UserModel, NewsModel
from django import forms
# Register your models here.

# 在保存时对密码进行加密
class UserAdminForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        raw_password = self.cleaned_data['user_pwd']
        if not raw_password.startswith('pbkdf2_'):  # 检查密码是否已经加密
            user.set_password(raw_password)
        if commit:
            user.save()
        return user

class UserModelAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ('id', 'user_name', 'user_mobile', 'user_pwd')
    search_fields = ('id', 'user_name')
    # readonly_fields = ('user_pwd',)
admin.site.register(UserModel, UserModelAdmin)

class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pub_date', 'content')
    search_fields = ('id', 'title')
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    readonly_fields = ('pub_date',)
admin.site.register(NewsModel, NewsModelAdmin)

admin.site.site_header = '博客管理'
admin.site.site_title = '博客管理'