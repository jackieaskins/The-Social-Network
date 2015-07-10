from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import StatusPostForm
from .models import StatusPost
from profiles.models import UserProfile


def home(request):

    context = {}

    if request.user.is_authenticated():
        form = StatusPostForm(request.POST or None)
        errors = None
        posts = StatusPost.objects.all().filter(user=request.user.id).order_by('-post_date')

        try:
            UserProfile.objects.get(user=request.user.id)
        except UserProfile.DoesNotExist:
            return redirect(reverse('create_profile'))

        if form.is_valid():
            status_post = form.save(commit=False)
            status_post.user = request.user
            status_post.save()
            return redirect(reverse('home'))
        else:
            errors = form.errors

        context = {
            'form': form,
            'errors': errors,
            'posts': posts,
        }

    return render(request, 'network/index.html', context)
