from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Notification


@login_required
def view_notifications(request):
    notifications = Notification.objects.all().filter(user=request.user).filter(
        Q(status=0) | Q(status=1)).order_by('-send_date')

    context = {
        'notifications': notifications,
    }

    return render(request, 'notifications/notifications_view.html', context)


@login_required
def read_notification(request):
    if 'notification_id' in request.GET:
        notification_id = request.GET['notification_id']
        notification = Notification.objects.get(id=notification_id)
        if notification.status != 1:
            notification.status = 1
            notification.save()
        num_new = Notification.objects.all().filter(user=request.user).filter(status=0).count()
        if num_new == 0:
            num_new = ''
        return HttpResponse(num_new)
    else:
        return redirect('view_notifications')
