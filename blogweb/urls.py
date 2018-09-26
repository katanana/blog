from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from blogweb import views



# # 引入路由
# router = SimpleRouter()
# # 使用router注册的地址
# router.register(r'^essay_del', views.E_del)




urlpatterns = [
    url(r'^add-article/', views.add_article, name='add-article'),
    url(r'^add-category/', views.add_category, name='add-category'),
    url(r'^add-flink/', views.add_flink, name='add-flink'),
    url(r'^add-notice/', views.add_notice, name='add-notice'),
    url(r'^article/', views.article, name='article'),
    url(r'^category/', views.category, name='category'),
    url(r'^comment/', views.comment, name='comment'),
    url(r'^flink/', views.flink, name='flink'),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^loginlog/', views.loginlog, name='loginlog'),
    url(r'^manage-user/', views.manage_user, name='manage-user'),
    url(r'^notice/', views.notice, name='notice'),
    url(r'^readset/', views.readset, name='readset'),
    url(r'^setting/', views.setting, name='setting'),
    url(r'^update-article/(?P<e_id>\d+)/', views.update_article, name='update-article'),
    url(r'^update-category/', views.update_category, name='update-category'),
    url(r'^update-flink/', views.update_flink, name='update-flink'),
    url(r'^register/', views.register, name='register'),

]