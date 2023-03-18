from django.contrib import admin
from django.urls import path, include
from .views import index, article, url_reverse, login
from . import views

app_name = 'app1'

urlpatterns = [
    path('', index, name='index'),  # 首页
    path('article/<int:id>/', article, name='article'),  # 展示文章 (路径参数)
    path('url_reverse/', url_reverse, name='url_reverse'),  # 路由反向解析

    path('login/', views.login, name='login'),  # 登录

    path('register', views.register, name='register'),


    path('user/list/', views.user_list, name='user_list'),
    path('user/delete/', views.user_delete, name='user_delete'),  # user_list/user_delete/?id=<int:id>  为什么不用这样写
    # path('user/add/', views.user_add, name='user_add'),

    path('depart/list', views.depart_list, name='depart_list'),
    path('depart/delete/', views.depart_delete, name='depart_delete'),

    path('pretty/list/',views.pretty_list,name='pretty_list'),

]
