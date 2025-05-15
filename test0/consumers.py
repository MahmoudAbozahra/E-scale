import socket
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json


SCALE_IP = '192.168.1.56'
SCALE_PORT = 25

def clean_data(data):
    parts = data.split()
    numbers = []
    for part in parts:
        digits = ''.join([c for c in part if c.isdigit() or c == '.'])
        if digits:
            numbers.append(digits)
    if numbers :
        selected = numbers[1]
    else:
        return None
    
    digits_only = ''.join([c for c in selected if c.isdigit()])
    if not digits_only:
        return None
    
    if len(digits_only) <= 4:
        weight = int(digits_only) / 10
    else:
        weight = int(digits_only) / 100
    return weight

class ScaleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_reading = True
        asyncio.create_task(self.send_weight_loop())

    async def disconnect(self, close_code):
        self.keep_reading = False

    async def send_weight_loop(self):
        while self.keep_reading:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((SCALE_IP, SCALE_PORT))
                
                data = sock.recv(1024)
                sock.close()

                raw_data = data.decode().strip()
                print("Raw data from scale:", raw_data)

                cleaned_weight = clean_data(raw_data)
                print("Cleaned weight:", cleaned_weight)

                if cleaned_weight and cleaned_weight < 0:
                    await self.send(text_data=json.dumps({'error': 'وزن غير صالح'}))
                else:
                    await self.send(text_data=json.dumps({'weight': cleaned_weight}))
                
            except Exception as e:
                await self.send(text_data=json.dumps({'error': str(e)}))

            await asyncio.sleep(0.1)

