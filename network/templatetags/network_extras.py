from django import template

from ..models import StatusComment, PostLike, CommentLike

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def up_to_comma(natural_time):
    if ',' in natural_time:
        return natural_time.split(',')[0] + ' ago'
    else:
        return natural_time


@register.filter
def check_has_liked_post(user, post_id):
    likes = PostLike.objects.filter(status_post=post_id)
    liked = False
    for like in likes:
        if user == like.user:
            liked = True
    return liked


@register.filter
def check_has_liked_comment(user, comment_id):
    likes = CommentLike.objects.filter(status_comment=comment_id)
    liked = False
    for like in likes:
        if user == like.user:
            liked = True
    return liked


@register.filter
def get_post_likes_user_list(post_id):
    likes = PostLike.objects.filter(status_post=post_id)
    users = []

    for like in likes:
        users.append(like.user)

    return users


@register.filter
def get_comment_likes_user_list(comment_id):
    likes = CommentLike.objects.filter(status_comment=comment_id)
    users = []

    for like in likes:
        users.append(like.user)

    return users


@register.inclusion_tag('network/comments.html', takes_context=True)
def get_post_comments(context, post_id):
    comments = StatusComment.objects.filter(status_post=post_id)
    return {'user': context['user'], 'comments': comments}
