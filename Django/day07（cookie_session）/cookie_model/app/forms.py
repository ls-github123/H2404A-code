# 定义登录表单，简化数据处理复杂度，同时提高安全性
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)