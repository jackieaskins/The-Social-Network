from django.contrib import admin

from .models import StatusPost, StatusComment


class StatusCommentInline(admin.StackedInline):
    model = StatusComment


class StatusPostAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'text', 'likes', 'post_date')
    inlines = (StatusCommentInline, )


class StatusCommentAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'status_post', 'likes', 'text', 'post_date')

admin.site.register(StatusPost, StatusPostAdmin)
admin.site.register(StatusComment, StatusCommentAdmin)
