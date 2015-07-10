from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def create_profile(request):

    form = UserProfileForm(request.POST or None)
    errors = None
    profile_exists = True

    try:
        UserProfile.objects.get(user=request.user.id)
    except UserProfile.DoesNotExist:
        profile_exists = False

    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect(reverse('home'))
    else:
        errors = form.errors

    context = {
        'form': form,
        'errors': errors,
        'profile_exists': profile_exists,
    }

    return render(request, 'profiles/profile_create.html', context)
