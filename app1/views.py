from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from . import models
from app1 import forms
from utils.Pagination import Pagination


# 视图函数
# Create your views here.
def index(request):
    data = {
        "a": 1,
        "b": 2.22,
        "c": True,
    }
    return render(request, "index.html", data)


def article(request, id):
    article = f"这是第{id}篇文章"
    data = {
        "article": article,
    }
    return render(request, "app1/article.html", data)


def url_reverse(request):
    return render(request, "app1/url_reverse.html")


def login(request):
    """
    实现简单的登录
    """
    data = {
        "username": "",
        "password": "",
        "msg": "",
    }
    if request.method == "POST":
        username = request.POST.get("username")
        data["username"] = username
        password = request.POST.get("password")
        data["password"] = password

        # 重定向
        if username == "01" and password == "01":
            return redirect("app1:article", 33)
        data["msg"] = "用户名或密码错误"
    return render(request, "app1/login.html", data)


@require_http_methods(["GET", "POST"])
def register(request):
    print(request.POST)
    return render(request, 'app1/register.html')


@require_http_methods(["GET", "POST"])
def user_list(request):
    users= models.UserInfo.objects.all()
    page_obj=Pagination(request,users,page_size=2)

    context = {
        'users': page_obj.page_queryset,
        'page_str':page_obj.html(),
        'user_form': forms.UserInfoModelForm()
    }
    if request.method == "POST":
        form = forms.UserInfoModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    # return redirect("app1:user_list")
    elif request.method == "PUT":
        pass
    return render(request, 'app1/user.html', context)


def user_delete(request):
    id = request.GET.get("id")
    # 根据id删除
    models.UserInfo.objects.filter(id=id).user_delete()
    return redirect("app1:user_list")


@require_http_methods(["GET", "POST"])
def depart_list(request):
    if request.method == "POST":
        title = request.POST.get("title")  # 这个title是模板中from表单里面的name
        # 创建数据
        models.Department.objects.create(title=title)
        return redirect("app1:depart_list")
    titles = models.Department.objects.all()
    return render(request, 'app1/depart.html', {'titles': titles})


def depart_delete(request):
    # /depart_list/user_delete/?id=    通过构造url的方式传递参数
    id = request.GET.get("id")
    # 根据id删除
    models.Department.objects.filter(id=id).user_delete()
    return redirect("app1:depart_list")


@require_http_methods(["GET", "POST"])
def pretty_list(request):
    # for i in range(1,100):
    #     models.PrettyNum.objects.create(phone='16607664565',price=100,level=1,status=1)

    data_dict = {}
    # /pretty_list/?q=1
    search_data = request.GET.get('q', '')

    if search_data:
        data_dict['search_data'] = search_data

    queryset = models.PrettyNum.objects.all().order_by('-level')
    page_obj = Pagination(request, queryset)

    context = {
        'search_data': search_data,
        'pretty': page_obj.page_queryset,  # 当前页的数据
        'page_str': page_obj.html(),  # 页码的html标签
        'forms': forms.PrettyNumModelForm(),
    }
    # POST请求添加数据
    if request.method == "POST":
        form = forms.PrettyNumModelForm(request.POST)
        context['forms'] = form
        if form.is_valid():
            form.save()
            return redirect("app1:pretty_list")
        else:
            print(form.errors)

    return render(request, 'app1/pretty.html', context=context)
