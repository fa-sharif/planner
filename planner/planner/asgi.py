import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planner.settings')
django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from planner.middleware import JWTAuthMiddlewareStack  # اینو درست ایمپورت کن
from tasks.routing import websocket_urlpatterns  # از tasks.routing ایمپورت کن



# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":JWTAuthMiddlewareStack(  # استفاده از middleware سفارشی
        URLRouter(websocket_urlpatterns)
    ),
})

