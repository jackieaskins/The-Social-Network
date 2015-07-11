from django.utils.timezone import now
from django.conf import settings
from django.db import models

from profiles.models import UserProfile


class StatusPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_profile = models.ForeignKey(UserProfile)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s - %s: %s" % (self.user, self.post_date, self.text[:50])
