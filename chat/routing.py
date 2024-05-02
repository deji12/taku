from django.urls import path, re_path
from .consumers import *

websocket_urlpatterns = [
    path('ws/message/<int:room_id>/', ChatConsumer.as_asgi()),

]