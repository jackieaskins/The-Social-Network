from django.contrib import admin

from .models import StatusPost


class StatusPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'likes', 'post_date')

admin.site.register(StatusPost, StatusPostAdmin)
