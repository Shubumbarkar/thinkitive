import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Document
from .utils import get_ai_suggestions  
class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.room_group_name = f'document_{self.doc_id}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data['content']
        try:
            document = Document.objects.get(id=self.doc_id)
            document.content = content
            document.save()
        except Document.DoesNotExist:
            print(f"Document with id {self.doc_id} does not exist.")
        suggestions = get_ai_suggestions(content)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'document_update',
                'content': content,
                'suggestions': suggestions,
            }
        )
    async def document_update(self, event):
        content = event['content']
        suggestions = event.get('suggestions', "")
        await self.send(text_data=json.dumps({
            'content': content,
            'suggestions': suggestions,
        }))