from django.db import models

# 创建用户表
class Users(models.Model):
    u_name = models.CharField(max_length=20, unique=True)
    u_pwd = models.CharField(max_length=225, unique=True)
    u_create_time = models.DateTimeField(auto_now_add=True)
    u_login_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'users'



class UserTicket(models.Model):
    user = models.ForeignKey(Users, related_name='u0')
    ticket = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(default=None)

    class Meta:
        db_table = 'user_ticket'


# 栏目表
class Part(models.Model):
    p_name = models.CharField(max_length=20, unique=True)
    p_alias = models.CharField(max_length=20, unique=True)
    p_keyword = models.CharField(max_length=20, unique=True)
    p_description = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'part'


# 创建文章表
class Essay(models.Model):
    e_name = models.CharField(max_length=50, unique=True)
    e_label = models.CharField(max_length=30, unique=False)
    e_content = models.TextField(max_length=30)
    e_create_time = models.DateTimeField(auto_now_add=True)
    e_operate_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)
    # 文章和用户的关系是一对多
    e_auth = models.ForeignKey(Users, related_name='u1')
    # e_u = models.ManyToManyField(Users, related_name='e_u')
    # 栏目和文章的关系是一对多
    e_part = models.ForeignKey(Part, related_name='ess')


    class Meta:
        db_table = 'essay'


# 创建公告表
class Notice(models.Model):
    n_name = models.CharField(max_length=50, unique=True)
    n_create_time = models.DateTimeField(auto_now_add=True)
    # 公告和用户的关系是一对多
    n_auth = models.ForeignKey(Users, related_name='u2')
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'notice'


# 创建评论表
class Comment(models.Model):
    c_name = models.CharField(max_length=50, unique=True)
    c_create_time = models.DateTimeField(auto_now_add=True)
    # 评论和用户的关系是一对多
    c_auth = models.ForeignKey(Users, related_name='u3')
    c_com = models.ForeignKey(Essay, related_name='c1')
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'comment'


