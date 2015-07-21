from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StatusPostForm, StatusCommentForm
from .models import StatusComment, StatusPost
from profiles.models import UserProfile


def home(request):

    context = {}

    if request.user.is_authenticated():

        try:
            UserProfile.objects.get(user=request.user.id)
        except UserProfile.DoesNotExist:
            return redirect('create_profile')

    comment_forms = {}
    errors = None

    posts = StatusPost.objects.filter(user=request.user.id)
    for post in posts:
        comment_forms[post.id] = StatusCommentForm()

    if 'post_form_error' in request.session:
        request.session.pop('post_form_error')
        post_form = StatusPostForm(request.POST)

        post_form.is_valid()
        errors = post_form.errors
    elif 'add_comment_redirect_post_id' in request.session:
        post_id = int(request.session.pop('add_comment_redirect_post_id'))
        comment_forms[post_id] = StatusCommentForm(request.POST)

        comment_form = comment_forms[post_id]
        comment_form.is_valid()
        errors = comment_form.errors

        post_form = StatusPostForm()
    else:
        post_form = StatusPostForm()

    context = {
        'post_form': post_form,
        'errors': errors,
        'posts': posts,
        'comment_forms': comment_forms,
    }

    return render(request, 'network/index.html', context)


@login_required
def add_post(request):
    if request.method != 'POST':
        return redirect('home')

    post_form = StatusPostForm(request.POST)

    if post_form.is_valid():
        status_post = post_form.save(commit=False)
        status_post.user = request.user
        status_post.save()

        if request.is_ajax():
            return HttpResponse()
    else:
        if request.is_ajax():
            error_msg = "<strong>Hey there! I don't think you typed anything...</strong>"
            error = '<p id="error_1_id_text" class="help-block">%s</p>' % error_msg
            return HttpResponse(error)

        request.session['post_form_error'] = post_form.errors

    return redirect('home')


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

        if request.is_ajax():
            comments = StatusComment.objects.filter(status_post=post_id)
            return render(request, 'network/comments.html', {'comments': comments})
    else:
        if request.is_ajax():
            error_msg = "<strong>Did you change your mind? You didn't type anything...</strong>"
            error = '<p id="error_1_id_text" class="help-block">%s</p>' % error_msg
            return HttpResponse(error)

        request.session['add_comment_redirect_post_id'] = post_id

    return redirect('home')
