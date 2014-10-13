from django.contrib import admin
from message.models import Message, Receiver

admin.site.register(Message)
admin.site.register(Receiver)