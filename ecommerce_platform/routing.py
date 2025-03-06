import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from store.consumers import InventoryConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_platform.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/inventory/", InventoryConsumer.as_asgi()),
    ]),
})
