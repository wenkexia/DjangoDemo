from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from users import models

class UserForm(forms.Form):
    username = forms.CharField(label="账号", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码', widget=CaptchaTextInput(attrs={'class': 'form-control'}))


# # 使用ModelForm编写表单
# class LoginModelForm(forms.ModelForm):
#     class Mate:
#         # 绑定模型类
#         model = models.User
#         exclude = [c_time]

        


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="账号",
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="密码",
        max_length=16,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="确认密码",
        max_length=16,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(
        label='验证码', widget=CaptchaTextInput(attrs={'class': 'form-control'}))
