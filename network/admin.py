from django.contrib import admin

from .models import StatusPost, StatusComment, PostLike, CommentLike


class StatusCommentInline(admin.StackedInline):
    model = StatusComment


class PostLikeInline(admin.TabularInline):
    model = PostLike


class CommentLikeInline(admin.TabularInline):
    model = CommentLike


class StatusPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'post_date')
    inlines = (StatusCommentInline, PostLikeInline)


class StatusCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'status_post',  'post_date')
    inlines = (CommentLikeInline, )


admin.site.register(StatusPost, StatusPostAdmin)
admin.site.register(StatusComment, StatusCommentAdmin)
