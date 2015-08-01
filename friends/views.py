from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Friendship


@login_required
def view_friends(request, username):
    user = get_object_or_404(User, username=username)

    user_friends = Friendship.objects.filter(from_user=user).filter(status=1)

    return render(request, 'friends/friends_view.html',
                  {'friends_user': user, 'user_friends': user_friends})


@login_required
def find_friends(request):
    results = []

    if request.method == 'POST':
        query = request.POST.get('query', None)
        if query:
            for term in query.split():
                results.extend(User.objects.filter(
                    Q(first_name__icontains=term) |
                    Q(last_name__icontains=term) |
                    Q(username__icontains=term)
                ))
            results = list(set(results))
        else:
            results.append(0)

    return render(request, 'friends/friend_find.html', {'results': results})
