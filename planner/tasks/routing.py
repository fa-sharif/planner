from django.urls import path
from .consumers import TaskConsumer

websocket_urlpatterns = [
    path("ws/notifications/", TaskConsumer.as_asgi()),
]
