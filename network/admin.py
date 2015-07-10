from django.contrib import admin

from .models import StatusPost, UserProfile


class StatusPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'likes', 'post_date')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'gender', 'profile_picture')

admin.site.register(StatusPost, StatusPostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
