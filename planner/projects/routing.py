from django.urls import path
from .consumers import PlannerConsumer

websocket_urlpatterns = [
    path('ws/planner/', PlannerConsumer.as_asgi()),
]
