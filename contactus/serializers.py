from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at', 'deletion_token']
        read_only_fields = ['id', 'deletion_token', 'created_at']
        extra_kwargs = {
            'name': {'help_text': 'Enter your full name'},
            'email': {'help_text': 'Enter a valid email address'},
            'subject': {'help_text': 'Enter the subject of your message'},
            'message': {'help_text': 'Enter your message here', 'style': {'base_template': 'textarea.html', 'rows': 4}},
        }