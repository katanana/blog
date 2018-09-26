from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from rest_framework import mixins, viewsets

from blogweb.models import Users, UserTicket, Essay, Notice, Comment, Part
from utils.functions import get_ticket, is_login


@is_login
def add_article(request):
    if request.method == 'GET':
        parts = Part.objects.all()
        return render(request, 'add-article.html', {'parts': parts})
    if request.method == 'POST':
        name = request.POST.get('title')
        content = request.POST.get('content')
        part = request.POST.get('category')
        label = request.POST.get('tags')
        Essay.objects.create(e_name=name, e_content=content, e_label=label, e_part_id=part, e_auth_id=1)
        return HttpResponseRedirect(reverse('boke:article'))


def add_category(request):
    if request.method == 'GET':
        return render(request, 'add-category.html')


def add_flink(request):
    if request.method == 'GET':
        return render(request, 'add-flink.html')


def add_notice(request):
    if request.method == 'GET':
        return render(request, 'add-notice.html')


def article(request):
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 1))
        # 从数据库中取出文章信息,返回给页面
        arts = Essay.objects.all()
        p = Paginator(arts, 5)
        page = p.page(page_num)
        return render(request, 'article.html', {'page': page})


def category(request):
    if request.method == 'GET':
        return render(request, 'category.html')


def comment(request):
    if request.method == 'GET':
        return render(request, 'comment.html')


def flink(request):
    if request.method == 'GET':
        return render(request, 'flink.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('userpwd')
        # 通过前端获取的数据查找数据表中是否存在该用户
        user = Users.objects.filter(u_name=username).first()
        if user:
            # 将user.password和form.cleaned_data['password']进行校验
            if check_password(pwd, user.u_pwd):
                # 校验用户名和密码都成功
                # 1. 设置cookie中的随机参数ticket --> auth.login()
                res = HttpResponseRedirect(reverse('blogweb:index'))
                # set_cookie(key, value, max_age='', expires='')
                ticket = get_ticket()
                res.set_cookie('ticket', ticket, max_age=100000)

                now = datetime.now()
                # 2. 设置user_ticker中存ticket和user的对应关系
                timespan = timedelta(days=1)
                UserTicket.objects.all().delete()
                UserTicket.objects.create(user=user, ticket=ticket, out_time=now)
                UserTicket.objects.filter(ticket=ticket).update(out_time=now + timespan)
                return res
        else:
            return render(request, 'login.html')


def loginlog(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def manage_user(request):
    if request.method == 'GET':
        return render(request, 'manage-user.html')


def notice(request):
    if request.method == 'GET':
        return render(request, 'notice.html')


def readset(request):
    if request.method == 'GET':
        return render(request, 'readset.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        # 获取前端页面提交的用户名和密码
        username = request.POST.get('username')
        pwd = make_password(request.POST.get('userpwd'))
        # 将用户名和密码存入用户表
        Users.objects.create(u_name=username, u_pwd=pwd)
        return HttpResponseRedirect(reverse('blogweb:login'))



def setting(request):
    if request.method == 'GET':
        return render(request, 'setting.html')


# @is_login
def update_article(request, e_id):
    if request.method == 'GET':
        parts = Part.objects.all()
        art = Essay.objects.get(pk=e_id)
        return render(request, 'update-article.html', {'art': art, 'parts': parts})
    if request.method == 'POST':
        name = request.POST.get('title')
        content = request.POST.get('content')
        part = request.POST.get('category')
        label = request.POST.get('tags')
        ess = Essay.objects.filter(pk=e_id)
        ess.update(e_name=name, e_content=content, e_label=label, e_part_id=part)
        return HttpResponseRedirect(reverse('blogweb:article'))


def update_category(request):
    if request.method == 'GET':
        return render(request, 'update-category.html')


def update_flink(request):
    if request.method == 'GET':
        return render(request, 'update-flink.html')



    class E_del(mixins.ListModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

        queryset = Essay.objects.all()

        def perform_destroy(self, instance):
            instance.is_delete = 1
            instance.save()