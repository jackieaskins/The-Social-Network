from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Notification(models.Model):

    TYPE_CHOICES = (
        (0, 'Friend Request'),
        (1, 'Message')
    )

    STATUS_CHOICES = (
        (0, 'Unread'),
        (1, 'Read')
    )

    to_user = models.ForeignKey(User)
    type_id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    content = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(default=0, choices=STATUS_CHOICES)
    send_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s: %s - %s" % (self.get_type_id_display(), self.to_user, self.content)


class FriendRequest(Notification):

    from_user = models.ForeignKey(User, related_name='sent_requests')

    def __init__(self, *args, **kwargs):
        super(FriendRequest, self).__init__(*args, **kwargs)
        self._meta.get_field('type_id').default = 0

    def save(self, *args, **kwargs):
        self.type_id = 0
        if (not self.content) and self.from_user:
            self.content = "%s wants to be your friend." % (self.from_user.get_full_name())
        super(FriendRequest, self).save(*args, **kwargs)
