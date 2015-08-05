from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


class Friendship(models.Model):

    STATUS_CHOICES = (
        (0, 'Pending...'),
        (1, 'Friends')
    )

    to_user = models.ForeignKey(User, related_name='friendship_set')
    from_user = models.ForeignKey(User, related_name='friends')
    status = models.PositiveSmallIntegerField(default=0, choices=STATUS_CHOICES)
    response_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "%s to %s" % (self.from_user.username, self.to_user.username)

    def save(self, *args, **kwargs):
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        if self.status != 0 and not self.response_date:
            self.response_date = now()
        super(Friendship, self).save(*args, **kwargs)
