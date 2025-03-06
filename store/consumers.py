import json

from channels.generic.websocket import WebsocketConsumer


class InventoryConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("InventoryConsumer: Connection accepted")

    def disconnect(self, close_code):
        print("InventoryConsumer: Disconnected with code", close_code)

    def receive(self, text_data):
        data = json.loads(text_data)
        print("InventoryConsumer received:", data)
        self.send(text_data=json.dumps({
            'message': 'Inventory updated',
            'data': data,
        }))
