from django.contrib import admin

from .models import FriendRequest, Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'type_id', 'content', 'status', 'send_date')


class FriendRequestAdmin(admin.ModelAdmin):
    fields = ('type_id', 'to_user', 'from_user', 'content', 'status', 'send_date')
    list_display = ('to_user', 'from_user', 'content', 'status', 'send_date')


admin.site.register(Notification, NotificationAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
