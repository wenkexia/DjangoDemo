from django.contrib import admin
from . import models


# 部门
@admin.register(models.Department)
class DepartmenttModelAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    # ordering = ('no', )


# 员工信息
#使用装饰器注册模型类
@admin.register(models.UserInfo)
class UserInfoModelAdmin(admin.ModelAdmin):
    # 列表中显示的字段
    list_display = ('name', 'gender', 'age', 'password', 'account',
                    'create_time', 'depart')
    # 可搜索字段
    search_fields = ('name', )
    # 列表中点击链接进入编辑页面的字段
    list_display_links = ('name', )
    # 编辑中的只读字段
    readonly_fields = ('create_time', )
    # 过滤器
    list_filter = ('create_time', )
    # 详细时间分层筛选
    date_hierarchy = 'create_time'
    ordering = ('create_time', )


@admin.register(models.PrettyNum)
class PrettyNumModelAdmin(admin.ModelAdmin):
    list_display = ('phone', 'price', 'level', 'status')
    search_fields = ('phone', )
    # 排序
    ordering = ('level', )
