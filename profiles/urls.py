from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/create/$', views.create_profile, name='create_profile'),
    url(r'^profiles/(?P<username>[\w.@+-]+)/$', views.view_profile, name='view_profile'),
]
