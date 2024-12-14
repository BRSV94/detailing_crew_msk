from django.shortcuts import render
from .models import ChatMessage

def chat_view(request):
    chat_messages = ChatMessage.objects.all().order_by('-created_at')

    return render(request, 'chat_template.html', {'chat_messages': chat_messages})