from django import template

from ..models import Notification

register = template.Library()


@register.simple_tag
def get_notification_count(user):
    notifications = Notification.objects.all().filter(user=user).filter(status=0)
    if notifications.count() > 0:
        return notifications.count()
    return ""
