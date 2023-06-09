# Generated by Django 4.1 on 2023-01-14 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='员工名字')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
                ('depart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.department', verbose_name='部门id')),
            ],
        ),
    ]
