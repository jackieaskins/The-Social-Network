from django import template

from ..models import StatusComment

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.inclusion_tag('network/comments.html')
def get_post_comments(post_id):
    comments = StatusComment.objects.filter(status_post=post_id)
    return {'comments': comments}
