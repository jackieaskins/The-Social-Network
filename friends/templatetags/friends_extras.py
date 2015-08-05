from django import template

from ..models import Friendship

register = template.Library()


@register.filter
def check_friend_status(from_user, to_user):
        friendship = Friendship.objects.filter(from_user=from_user).filter(to_user=to_user)

        return friendship[0].status
