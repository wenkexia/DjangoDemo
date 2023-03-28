
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    # path(r'^snippets/$', views.snippet_list),
    # path(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    path('', views.api_root),
    path('list/', views.snippet_list),
    path('detail/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)