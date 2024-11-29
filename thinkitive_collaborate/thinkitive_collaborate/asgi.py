import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from thinkitive_app.routing import websocket_urlpatterns  # Your app's routing file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collaborative_editor.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
