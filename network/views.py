from django.shortcuts import render, redirect

from network.forms import StatusPostForm


def home(request):

    form = StatusPostForm(request.POST or None)
    error = None

    if form.is_valid():
        status_post = form.save(commit=False)
        status_post.user = request.user
        status_post.save()
        return redirect('/')
    else:
        error = form.errors

    return render(request, 'network/index.html', {'form': form, 'errors': error})
