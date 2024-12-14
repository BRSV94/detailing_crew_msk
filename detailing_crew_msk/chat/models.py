from django.db import models



class ChatMessage(models.Model):
    sender = models.CharField(
        max_length=128,
    )
    message = models.TextField(
        max_length=1024,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
