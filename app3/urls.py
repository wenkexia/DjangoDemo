
from django.urls import path
from .views import index





app_name = 'app3'

urlpatterns = [
    path('', index, name='index'),  # 首页
]