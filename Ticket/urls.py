# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from App import routing  # Import the WebSocket routing configuration from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    # Other URL patterns for your project
    path('ws/vote/', include(routing.websocket_urlpatterns)),
]
