from datetime import datetime

from django.db import models


class User(models.Model):
    """
    用户信息
    """

    username = models.CharField('账号', max_length=16, unique=True)
    password = models.CharField('密码', max_length=16)
    email = models.EmailField('邮箱', unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['c_time']  # 元数据里定义用户按创建时间的反序排列，也就是最近的最先显示
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):  # 使用__str__帮助人性化显示对象信息
        return self.username