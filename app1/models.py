from django.db import models


class Department(models.Model):
    '''
    部门表
    '''
    title = models.CharField(verbose_name='部门名称', max_length=50)

    # 重新str方法
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    '''
    员工表
    '''
    name = models.CharField(verbose_name='员工名字', max_length=50)
    # 模板中用{{querryset对象.get_字段_display}}   get_字段_display() 模板会自己加（）
    # 在视图中，可以通过querryset对象.get_gender_display()获取到性别的中文描述
    gender_choices = ((1, '男'), (2, '女'))  # 用元组规定1男 2女
    gender = models.IntegerField(verbose_name='性别', choices=gender_choices)

    age = models.IntegerField(verbose_name='年龄', default=18)  # 默认值为18
    password = models.CharField(verbose_name='密码', max_length=64)

    # 最大长度为10，小数点后保留两位
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    # 在视图中，可以通过querryset对象.create_time.strftime("%Y-%m-%d")
    # 在模板中{{querryset对象.create_time|date:"Y-m-d H:i:s" }}
    create_time = models.DateTimeField(verbose_name='入职时间', auto_now_add=True)

    '''
    外键约束(只能是部门表的id)，to指定关联表,to_field指定关联的字段
    Django底层生成的列是：department_id

    如果部门表删除了，关联的用户有以下处理方式：
        on_delete=models.CASCADE  级联删除
        on_delete=models.SET_NULL  设置为空
    '''
    # querryset对象.外键字段(depart).关联表字段(title)  根据员工表的外键department_id查询所关联的部门表的数据
    depart = models.ForeignKey(verbose_name='部门id', to='Department', to_field='id', on_delete=models.SET_NULL,
                               null=True)


class PrettyNum(models.Model):
    '''
    靓号表
    '''
    phone = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格')
    level_choices = (
        # 第一个是数据库存储的值，第二个是显示的值
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),

    )
    level = models.SmallIntegerField(verbose_name='等级', choices=level_choices, default=1)

    status_choices = (
        (0, '未售'),
        (1, '已售'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=0)
