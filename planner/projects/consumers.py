# projects/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs

class PlannerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract token from query params
        query_params = parse_qs(self.scope['query_string'].decode())
        token = query_params.get('token', [None])[0]

        try:
            # Validate token
            UntypedToken(token)
            await self.accept()
        except InvalidToken:
            # Close connection if token is invalid
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle received data
        await self.send(text_data=json.dumps({
            'message': 'Message received',
            'data': data
        }))
