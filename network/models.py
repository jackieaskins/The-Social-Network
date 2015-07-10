from django.utils.timezone import now
from django.conf import settings
from django.db import models

PROF_PIC_ROOT = settings.MEDIA_ROOT + '/profile_pictures'


class StatusPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    post_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)

    def __str__(self):
        return "%s - %s: %s" % (self.user, self.post_date, self.text[:50])


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    profile_picture = models.ImageField(blank=True, upload_to='profile_pictures')

    def save(self, *args, **kwargs):
        if (not self.profile_picture) and (self.gender == 'M'):
            self.profile_picture = PROF_PIC_ROOT + '/default_male.png'
        elif (not self.profile_picture) and (self.gender == 'F'):
            self.profile_picture = PROF_PIC_ROOT + '/default_female.png'
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user
