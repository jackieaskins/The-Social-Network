from django import forms
from django.conf.urls import include, url
from django.contrib import admin

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationForm
from registration.users import UserModel, UsernameField

from network import views as network_views


class MyRegistrationForm(RegistrationForm):

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserModel()
        fields = ('first_name', 'last_name', UsernameField(), "email")

urlpatterns = [
    url(r'^$', network_views.home, name='home'),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=MyRegistrationForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
