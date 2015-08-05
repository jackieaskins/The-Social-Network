from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^friends/(?P<username>[\w.@+-]+)/', include([
        url(r'^$', views.view_friends, name='view_friends'),
        url(r'^accept/$', views.accept_request, name='accept_request'),
        url(r'^reject/$', views.reject_request, name='reject_request'),
        url(r'^edit_friendship/$', views.edit_friendship, name='edit_friendship'),
    ])),
    url(r'^friend/', include([
        url(r'^find/$', views.find_friends, name='find_friends'),
    ])),
]
