from django.db import models
from mdeditor.fields import MDTextField
class WeChatSet(models.Model):
    """ 基本配置 """
    title = models.CharField(verbose_name='标题', max_length=32)
    # conten = models.CharField(verbose_name='内容', max_length=32)
    conten = MDTextField()