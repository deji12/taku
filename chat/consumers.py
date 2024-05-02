import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import *
from assignment.models import Assignment, AssignmentMessages
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_id']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        
        event = {
            'type': 'send_message',
            'message':message,
        }
        
        await self.channel_layer.group_send(self.room_name, event)
    
    async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))
    
    @database_sync_to_async
    def create_message(self, data):
        get_room_by_name = Assignment.objects.get(id=data['room_id'])
        if not AssignmentMessages.objects.filter(message=data['message'], assignment=get_room_by_name).exists():
            new_message = AssignmentMessages(assignment=get_room_by_name, sender=User.objects.get(username=data['sender']), message=data['message'])
            new_message.save()
            
