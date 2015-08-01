from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^friends/(?P<username>[\w.@+-]+)/$', views.view_friends, name='view_friends'),
    url(r'^friend/find/$', views.find_friends, name='find_friends'),
]
