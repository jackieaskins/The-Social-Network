from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'content', 'status', 'send_date')

admin.site.register(Notification, NotificationAdmin)
