# planner/asgi.py

import os

from dotenv import load_dotenv

load_dotenv()  # این خط فایل .env رو لود می‌کنه

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planner.settings')

import django
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from tasks.routing import websocket_urlpatterns  # Import WebSocket routes
from planner.middleware import JWTAuthMiddleware



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planner.settings')
# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthMiddleware(
        URLRouter(
            websocket_urlpatterns  # Add WebSocket routes
        )
    ),
})

