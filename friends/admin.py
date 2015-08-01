from django.contrib import admin

from .models import Friendship


class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status', 'response_date')

admin.site.register(Friendship, FriendshipAdmin)
