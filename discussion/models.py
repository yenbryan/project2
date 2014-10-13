from django.db import models
from registration.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=125)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.name

class Discussion(models.Model):
    title = models.CharField(max_length=125)
    text = models.TextField()
    poster = models.ForeignKey(Profile, related_name="discussions")
    category = models.ForeignKey(Category, related_name="discussions")

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    poster = models.ForeignKey(Profile, related_name="comments")
    discussion = models.ForeignKey(Discussion, related_name='comments')

    def __unicode__(self):
        return self.text


