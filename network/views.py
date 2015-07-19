from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import StatusPostForm, StatusCommentForm
from .models import StatusPost, StatusComment
from profiles.models import UserProfile


def home(request):

    context = {}

    if request.user.is_authenticated():

        try:
            UserProfile.objects.get(user=request.user.id)
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

        comments = []
        comment_forms = {}
        errors = None

        posts = StatusPost.objects.filter(user=request.user).order_by('-post_date')
        for post in posts:
            comments += StatusComment.objects.filter(status_post=post.id).order_by('post_date')
            comment_forms[post.id] = StatusCommentForm()

        if 'add_comment_redirect_post_id' in request.session:
            post_id = int(request.session.pop('add_comment_redirect_post_id'))
            comment_forms[post_id] = StatusCommentForm(request.POST)

            comment_form = comment_forms[post_id]
            comment_form.is_valid()
            errors = comment_form.errors

            post_form = StatusPostForm()
        else:
            post_form = StatusPostForm(request.POST or None)

            if post_form.is_valid():
                status_post = post_form.save(commit=False)
                status_post.user = request.user
                status_post.save()
                return redirect('home')
            else:
                errors = post_form.errors

        context = {
            'post_form': post_form,
            'errors': errors,
            'posts': posts,
            'comments': comments,
            'comment_forms': comment_forms,
        }

    return render(request, 'network/index.html', context)


@login_required
def add_comment(request, post_id):

    if request.method != 'POST':
        return redirect('home')

    status_post = StatusPost.objects.get(id=post_id)

    comment_form = StatusCommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.status_post = status_post
        comment.user = request.user
        comment.save()
    else:
        request.session['add_comment_redirect_post_id'] = post_id

    return redirect('home')
