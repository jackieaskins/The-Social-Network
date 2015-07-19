from django.contrib.auth.models import User
from django.db import models

from sorl.thumbnail import ImageField


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(User, related_name='user_profile')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    profile_picture = ImageField(blank=True, upload_to='profile_pictures')

    def save(self, *args, **kwargs):
        if (not self.profile_picture) and (self.gender == 'M'):
            self.profile_picture = 'profile_pictures/default_male.png'
        elif (not self.profile_picture) and (self.gender == 'F'):
            self.profile_picture = 'profile_pictures/default_female.png'
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
