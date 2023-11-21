import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from django.contrib.auth.models import User
import re

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # Sanitize the room name by replacing spaces with underscores
        sanitized_room_name = re.sub(r'\s', '_', self.room_name)
        self.room_group_name = "chat_{}".format(sanitized_room_name)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def save_message_to_database(self, message_content, user_id):
        # Save message to the database with room information and user
        user = User.objects.get(id=user_id) if user_id else None
        Message.objects.create(content=message_content, room=self.room_name, user=user)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']

        # Ensure that the user is authenticated before accessing its ID
        if self.scope['user'].is_authenticated:
            user_id = str(self.scope['user'].id)
        else:
            user_id = None

        # Save message to the database with the current user
        await self.save_message_to_database(message_content, user_id)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message_content,
                'user_id': user_id,  # Pass the user ID to the group
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        # Retrieve user object based on user_id
        user = await self.get_user_by_id(user_id)

        # Send message to WebSocket with the username
        await self.send(text_data=json.dumps({
            'message': f'{user.username}: {message}'
        }))

    @database_sync_to_async
    def get_user_by_id(self, user_id):
        # Retrieve user object based on user_id
        return User.objects.get(id=user_id)



