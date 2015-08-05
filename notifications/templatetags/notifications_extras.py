from django import template

from ..models import Notification, FriendRequest

register = template.Library()


@register.simple_tag
def get_notification_count(user):
    notifications = Notification.objects.filter(to_user=user).filter(status=0)
    if notifications.count() > 0:
        return notifications.count()
    return ""


@register.filter
def check_is_friend_request(not_id):
    try:
        Notification.objects.get(id=not_id).friendrequest
        return True
    except FriendRequest.DoesNotExist:
        return False
