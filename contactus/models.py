from django.db import models
import uuid

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deletion_token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"