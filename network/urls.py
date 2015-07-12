from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)/add_comment/$', views.add_comment, name='add_comment'),
]
