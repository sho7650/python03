from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.user_list, name='user_list'),
    url(r'^list/$', views.account_list, name='account_list'),
]
