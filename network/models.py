from django.utils.timezone import now
from django.conf import settings
from django.db import models


class StatusPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s - %s: %s" % (self.user, self.post_date, self.text[:50])
