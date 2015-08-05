from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.timezone import now

from .models import Friendship
from notifications.models import FriendRequest


@login_required
def view_friends(request, username):
    user = get_object_or_404(User, username=username)

    user_friends = Friendship.objects.filter(from_user=user).filter(status=1)

    return render(request, 'friends/friends_view.html',
                  {'friends_user': user, 'user_friends': user_friends})


@login_required
def find_friends(request):
    results = []
    query = None

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
    elif request.method == 'GET':
        if 'query' in request.GET:
            query = request.GET['query']
            for term in query.split():
                results.extend(User.objects.filter(
                    Q(first_name__icontains=term) |
                    Q(last_name__icontains=term) |
                    Q(username__icontains=term)
                ))
            results = list(set(results))

    return render(request, 'friends/friend_find.html', {'results': results, 'search_terms': query})


@login_required
def edit_friendship(request, username):
    if request.method != 'POST':
        return redirect('home')

    from_user = request.user
    to_user = get_object_or_404(User, username=username)

    redirect_to = request.GET.get('next', None)
    query = request.GET.get('query', None)

    try:
        friendship = Friendship.objects.get(from_user=from_user, to_user=to_user)
        if friendship.status == 0:
            friendship.delete()
            FriendRequest.objects.filter(from_user=from_user).filter(to_user=to_user).delete()
        elif friendship.status == 1:
            Friendship.objects.get(from_user=to_user, to_user=from_user).delete()
            FriendRequest.objects.filter(from_user=from_user).filter(to_user=to_user).delete()
            FriendRequest.objects.filter(from_user=to_user).filter(to_user=from_user).delete()
            friendship.delete()
    except Friendship.DoesNotExist:
        Friendship.objects.create(from_user=from_user, to_user=to_user, status=0)
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)

    if redirect_to:
        if query:
            redirect_to += ('?query=' + query)
        return redirect(redirect_to)
    else:
        return redirect('home')


@login_required
def accept_request(request, username):
    if request.method != 'POST':
        return redirect('home')

    redirect_to = request.GET.get('next', None)

    to_user = request.user
    from_user = get_object_or_404(User, username=username)
    response_time = now()

    try:
        friendship = Friendship.objects.get(from_user=from_user, to_user=to_user)
        friendship.status = 1
        friendship.response_date = response_time
        friendship.save()

        new_friendship, created = Friendship.objects.get_or_create(from_user=to_user,
                                                                   to_user=from_user)
        new_friendship.status = 1
        new_friendship.response_date = response_time
        new_friendship.save()

        FriendRequest.objects.filter(from_user=from_user).filter(to_user=to_user).delete()
        FriendRequest.objects.filter(from_user=to_user).filter(to_user=from_user).delete()
    except Friendship.DoesNotExist:
        pass

    if redirect_to:
        return redirect(redirect_to)
    else:
        return redirect('home')


def reject_request(request, username):
    if request.method != 'POST':
        return redirect('home')

    redirect_to = request.GET.get('next', None)

    to_user = request.user
    from_user = get_object_or_404(User, username=username)

    Friendship.objects.filter(from_user=from_user).filter(to_user=to_user).delete()
    Friendship.objects.filter(from_user=to_user).filter(to_user=from_user).delete()
    FriendRequest.objects.filter(from_user=from_user).filter(to_user=to_user).delete()
    FriendRequest.objects.filter(from_user=to_user).filter(to_user=from_user).delete()

    if redirect_to:
        return redirect(redirect_to)
    else:
        return redirect('home')
