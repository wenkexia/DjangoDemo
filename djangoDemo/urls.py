"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include, re_path

from django.views.static import serve
from djangoDemo.settings import MEDIA_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("app1.urls"), name='app1'),
    path('users/', include('users.urls'), name='users'),
    path('captcha', include('captcha.urls')),
    # path('blog/',include('blog.urls'),name='blog'),
    path('mdeditor/',
         include(('mdeditor.urls', 'mdeditor'),
                 namespace='mdeditor')),  # 配置编辑器路由
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': MEDIA_ROOT}),  # 添加上传文件路径
]
