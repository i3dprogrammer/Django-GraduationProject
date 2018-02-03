import json
from .models import Session
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import AsyncToSync
from channels.layers import get_channel_layer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        AsyncToSync(self.channel_layer.group_add)("chat", self.channel_name)
    
    def receive(self, text_data=None, byte_data=None):
        self.send(text_data='Hello world')

    def disconnect(self):
        pass