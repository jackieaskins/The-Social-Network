from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class StatusPost(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return "%s - %s" % (self.user, self.text[:50])


class StatusComment(models.Model):
    status_post = models.ForeignKey(StatusPost)
    user = models.ForeignKey(User)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return "%s - %s" % (self.user, self.text[:50])
