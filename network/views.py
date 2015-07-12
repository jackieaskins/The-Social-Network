from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import StatusPostForm, StatusCommentForm
from .models import StatusPost, StatusComment
from profiles.models import UserProfile


def home(request):

    context = {}

    if request.user.is_authenticated():
        post_form = StatusPostForm(request.POST or None)
        comment_form = StatusCommentForm()
        errors = None
        comments = []
        posts = StatusPost.objects.all().filter(user=request.user.id).order_by('-post_date')
        user_profile = None

        for post in posts:
            comments += StatusComment.objects.all().filter(status_post=post.id)

        try:
            user_profile = UserProfile.objects.get(user=request.user.id)
        except UserProfile.DoesNotExist:
            return redirect(reverse('create_profile'))

        if post_form.is_valid():
            status_post = post_form.save(commit=False)
            status_post.user = request.user
            status_post.user_profile = user_profile
            status_post.save()
            return redirect(reverse('home'))
        else:
            errors = post_form.errors

        context = {
            'comment_form': comment_form,
            'post_form': post_form,
            'errors': errors,
            'posts': posts,
            'comments': comments,
        }

    return render(request, 'network/index.html', context)


@login_required
def add_comment(request, post_id):

    if request.method != 'POST':
        return redirect(reverse('home'))

    post_form = StatusPostForm()
    comment_form = StatusCommentForm(request.POST)
    errors = None
    comments = []
    posts = StatusPost.objects.all().filter(user=request.user.id).order_by('-post_date')
    user_profile = None
    status_post = StatusPost.objects.get(id=post_id)

    for post in posts:
        comments += StatusComment.objects.all().filter(status_post=post.id)

    try:
        user_profile = UserProfile.objects.get(user=request.user.id)
    except UserProfile.DoesNotExist:
        return redirect(reverse('create_profile'))

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.status_post = status_post
        comment.user = request.user
        comment.user_profile = user_profile
        comment.save()
    else:
        errors = comment_form.errors
        context = {
            'comment_form': comment_form,
            'post_form': post_form,
            'errors': errors,
            'posts': posts,
            'comments': comments,
        }
        return render(request, 'network/index.html', context)

    return redirect(reverse('home'))
