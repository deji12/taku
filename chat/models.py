from django.db import models
from users.models import User
#Vedio calls
class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class VideoCall(models.Model):
    recipient = models.ForeignKey(User, related_name='received_video_calls', on_delete=models.CASCADE)
    caller = models.ForeignKey(User, related_name='made_video_calls', on_delete=models.CASCADE)
    room_name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='pending')  # status can be 'pending', 'accepted', 'rejected', etc.

    def __str__(self):
        return f"Video Call: {self.caller.username} to {self.recipient.username}"
    
#messages
class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)