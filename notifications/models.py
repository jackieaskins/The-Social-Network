from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Notification(models.Model):
    user = models.ForeignKey(User)
    notification_type = models.CharField(max_length=80)
    content = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(default=0)
    send_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s: %s" % (self.notification_type, self.content)
