
from django.urls import path
from users import views

from django.contrib import admin



app_name = 'users'

from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

#
# urlpatterns = [
#     path('', views.index, name='index'),  # 首页
#     path('login/', views.login, name='login'),  # 登录
#
#     path('admin', admin.site.urls),
#
#     path('index/', views.index),
#     path('register/', views.register),
#     path('logout/', views.logout),
# ]