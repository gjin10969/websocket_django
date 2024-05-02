from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
import asyncio

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Start a loop to send random messages every 3 seconds
        self.loop_task = asyncio.create_task(self.send_random_messages())



    async def send_random_messages(self):
        while True:
            await self.send(json.dumps({'message': randint(1, 100)}))
            await asyncio.sleep(3)
