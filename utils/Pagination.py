'''
自定义分页组件
(基于bootstrp5)
(视图中使用)
#根据情况筛选的所欲数据
queryset = models.Book.objects.all()
#实例化分页对象
page_obj = Pagination(request,queryset,page_size=10,page_param='page',plus=5)

context ={
    'search_data':search_data,
    'pretty':page_obj.page_queryset,   #当前页的数据
    'page_str':page_obj.html(),   #页码的html标签
}


(模板中使用)
<!--显示数据  -->
{% for p in pretty %}
    {{p.id}}
{% endfor %}

<!--分页  -->
<ul class="pagination">
<!-- 在后端生成的html -->
    {{page_str}}
</ul>
'''
from django.utils.safestring import mark_safe
class Pagination(object):

    '''
    description:
    event:
    param {*} self
    param {*} request   请求对象
    param {*} page_size 每页显示的条数
    param {*} page_param 页码参数
    param {*} plus 页码前后显示的页码数
    return {*}
    '''
    def __init__(self,request,queryset,page_size=10,page_param='page',plus=5) :

        import copy
        # 带着原来的参数，加上别的参数，拼接url
        # /?q=888&page=1
        query_dict = copy.deepcopy(request.GET)  # 深拷贝一份
        query_dict._mutable = True  # 设置这个为True,即可设置url
        self.query_dict = query_dict
        self.page_param =page_param
        # query_dict.setlist('page', [1])
        # print(query_dict.urlencode())


        # 获取当前页码,就是url中的page参数(/?page=1)
        page = request.GET.get(page_param,"1")
        # 判断是否是十进制数字
        # 这里不能直接转换成int类型，因为如果用户输入的不是数字，会报错
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page= page
        self.page_size= page_size
        # 根据用户想要的页码，计算出起始位置
        self.start = (page-1)*page_size
        self.end = page*page_size

        self.page_queryset = queryset[self.start:self.end]
        # 总条数
        self.total_count = queryset.count()
        # 总页数
        total_page_count,div = divmod(self.total_count,page_size)
        if div:
            total_page_count+=1
        self.total_page_count = total_page_count
        self.plus = plus
    def html(self):
        # 计算出，显示当前页的前5页和后5页
        if self.total_page_count<=2*self.plus+1:
            # 当数据库的数据较少,总页数小于11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 当前页小于等于5
            if self.page <=self.plus:
                start_page = 1
                end_page = 2*self.plus+1
            else:
                # 当前页大于5
                # 当前页+5大于总页数
                if(self.page+self.plus)>self.total_page_count:
                    start_page =  self.total_page_count-2*self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page+self.plus
        # 页码
        page_list= []
        self.query_dict.setlist(self.page_param, [1])
        # print(query_dict.urlencode())   #urlencode拼接后的url
        page_list.append(f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">首页</a></li>')

        if self.page>1:
            self.query_dict.setlist(self.page_param, [self.page-1])
            prev = f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">上一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">上一页</a></li>'

        page_list.append(prev)
        # 页面
        for i in range(start_page,end_page):
            self.query_dict.setlist(self.page_param, [i])
            # 在当前页时，高亮
            if i ==self.page:
                ele =f'<li class="active page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">{i}</a></li>'
            else:
                ele = f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">{i}</a></li>'
            page_list.append(ele)
        # 下一页
        if self.page<self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page+1])
            prev = f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">下一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">下一页</a></li>'
        page_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_list.append(f'<li class="page-item"><a class="page-link" href="?{self.query_dict.urlencode()}">尾页</a></li>')
        # form表单基于ajax来传参
        search_str ="""
        <li>
            <form  method="get">
                <input class="form-control " type="text" placeholder="页码">
                <button class="btn btn-outline-success" type="submit">跳转</button>
            </form>
        </li>
        """

        page_list.append(search_str)
        # mark_safe使得页面中的html代码生效
        page_str = mark_safe(''.join(page_list))
        return page_str