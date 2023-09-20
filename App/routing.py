# App/routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/vote/', consumers.VoteConsumer.as_asgi()),
]
