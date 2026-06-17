from rest_framework import serializers
from .models import ActivityLog


class ActivityLogSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ActivityLog
        fields = ['id', 'user', 'user_username', 'action', 'action_description', 'content_type',
                  'object_id', 'object_name', 'old_value', 'new_value', 'ip_address', 'created_at']
        read_only_fields = ['created_at']
