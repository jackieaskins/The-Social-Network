from django.conf import settings
from django.db import models


class StatusPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s" % (self.user, self.text)[:50]
