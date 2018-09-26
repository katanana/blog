
import random

from django.http import HttpResponseRedirect
from django.urls import reverse

from blogweb.models import UserTicket


def get_ticket():
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket


def is_login(func):

    def check(request):
        ticket = request.COOKIES.get('ticket')
        if ticket:
            # 通过user_ticket获取对象
            user_ticket = UserTicket.objects.filter(ticket=ticket).first()
            if user_ticket:
                user = user_ticket.user.u_name
                return func(request)
            else:
                # ticket参数错误, 则跳转登录
                return HttpResponseRedirect(reverse('boke:login'))
    return check