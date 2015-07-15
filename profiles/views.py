from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect

from datetime import date

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


@login_required
def view_profile(request, username):
    try:
        user_profile = UserProfile.objects.get(user=request.user.id)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')

    today = date.today()
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    user_profile = UserProfile.objects.get(user=user.id)
    born = user_profile.birthday
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    context = {
        'user_profile': user_profile,
        'age': age,
    }
    return render(request, 'profiles/profile_view.html', context)
