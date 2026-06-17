from rest_framework import serializers
from .models import Notification, EmailLog


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'notification_type', 'title', 'message', 'is_read',
                  'read_at', 'action_url', 'related_object_id', 'created_at']
        read_only_fields = ['created_at', 'read_at']


class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = ['id', 'recipient', 'subject', 'status', 'email_type', 'related_object_id', 'created_at', 'sent_at']
        read_only_fields = ['created_at', 'sent_at']
