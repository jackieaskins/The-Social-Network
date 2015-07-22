from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^comment/(?P<comment_id>\d+)/', include([
        url(r'^like/$', views.like_comment, name='like_comment'),
    ])),
    url(r'^post/(?P<post_id>\d+)/', include([
        url(r'^add_comment/$', views.add_comment, name='add_comment'),
        url(r'^like/$', views.like_post, name='like_post'),
    ])),
    url(r'^add_post/$', views.add_post, name='add_post'),
]
