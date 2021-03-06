from django.contrib import admin
from django.contrib.auth.models import User

from sorl.thumbnail.admin import AdminImageMixin

from .models import UserProfile


class UserProfileInline(AdminImageMixin, admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('user', 'birthday', 'gender', 'profile_picture')


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
