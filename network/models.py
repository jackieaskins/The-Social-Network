from django.db import models
from django.utils.timezone import now

from profiles.models import UserProfile


class StatusPost(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s - %s" % (self.user_profile.user, self.text[:50])


class StatusComment(models.Model):
    status_post = models.ForeignKey(StatusPost)
    user_profile = models.ForeignKey(UserProfile)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s - %s" % (self.user_profile.user, self.text[:50])
