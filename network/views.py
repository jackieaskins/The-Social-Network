from django.shortcuts import render, redirect

from network.forms import StatusPostForm
from network.models import StatusPost


def home(request):

    context = {}

    if request.user.is_authenticated():
        form = StatusPostForm(request.POST or None)
        error = None
        posts = StatusPost.objects.all().filter(user=request.user).order_by('-post_date')

        if form.is_valid():
            status_post = form.save(commit=False)
            status_post.user = request.user
            status_post.save()
            return redirect('/')
        else:
            error = form.errors

        context = {
            'form': form,
            'errors': error,
            'posts': posts,
        }

    return render(request, 'network/index.html', context)
