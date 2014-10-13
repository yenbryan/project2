from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    about_me = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class ProfilePicture(models.Model):
    image = models.ImageField(upload_to='media/profile_picutures',
                              blank=True,
                              null=True)
    description = models.CharField(max_length=140,
                                   blank=True,
                                   null=True)
    default_picture = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name='profile_pictures')
