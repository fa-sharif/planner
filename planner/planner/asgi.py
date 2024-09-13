# planner/asgi.py
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from projects.routing import websocket_urlpatterns  # Import WebSocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planner.settings')
application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns  # Add WebSocket routes
#         )
#     ),
# })
