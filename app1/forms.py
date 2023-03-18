from django import forms
from app1 import models
from django.core.validators import RegexValidator

class UserInfoModelForm(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = "__all__"

        # # 定制内部属性
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control'}),
        # }


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            # 给所有的字段添加class属性
            field.widget.attrs = {'class':"form-control",'placeholder':field.label}
            # print(name,field)



class PrettyNumModelForm(forms.ModelForm):
    # phone = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    #     )
    class Meta:
        model = models.PrettyNum
        fields = "__all__"
        # fields = ['phone',"price",'level','status']



    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs = {'class':'form-control','placeholder':field.label}
    # 钩子函数
    def clean_phone(self):
        txt_phone = self.cleaned_data.get('phone')
        if len(txt_phone) != 11:
            raise forms.ValidationError('手机号格式错误')   #抛出异常

        return txt_phone
