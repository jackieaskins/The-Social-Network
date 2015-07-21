from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<post_id>\d+)/', include([
        url(r'^add_comment/$', views.add_comment, name='add_comment'),
    ])),
    url(r'^add_post/$', views.add_post, name='add_post'),
]
