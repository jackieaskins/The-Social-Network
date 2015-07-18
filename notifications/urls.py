from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_notifications, name='view_notifications'),
    url(r'^read/$', views.read_notification, name='read_notification')
]
