from django.db import models
from registration.models import Profile


# class MessageRoom(models.Model):

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Profile, related_name='messages')
    # message_room = models.ForeignKey(MessageRoom, related_name='messages')

    def __unicode__(self):
        return self.title

# Couldn't recipient just be a field on Message?
class Receiver(models.Model):
    message = models.ForeignKey(Message, related_name='receivers')
    recipient = models.ForeignKey(Profile, related_name='receivers')

    def __unicode__(self):
        return self.recipient.username
