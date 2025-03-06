import os

import django
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from ecommerce_platform.routing import application as channels_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_platform.settings')
django.setup()

application = channels_application
