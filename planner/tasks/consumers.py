from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.group_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
            await self.send(text_data=json.dumps({"message": "connected"}))
        else:
            await self.close()

    async def disconnect(self, close_code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # برای تست دستی از سمت کلاینت (مثلاً test_websocket.py)
        data = json.loads(text_data)
        message = data.get("message", "")
        await self.send(text_data=json.dumps({"message": f"You said: {message}"}))

    async def task_notification(self, event):
        await self.send(text_data=json.dumps(event["data"]))
