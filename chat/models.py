# chat/models.py
from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    room = models.CharField(max_length=255, default="default_room")

    def __str__(self):
        return f"{self.room} - {self.user} - {self.content}"
    

from django.urls import reverse

class Room(models.Model):
    book_title = models.CharField(max_length=255, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    current_goal = models.CharField(max_length=255, blank=True, null=True)
    next_discussion = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])    