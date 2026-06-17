from rest_framework import serializers
from .models import Message, Proposal, Feedback


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    receiver_username = serializers.CharField(source='receiver.username', read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'receiver', 'receiver_username', 
                  'project', 'subject', 'content', 'is_read', 'read_at', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'read_at']


class ProposalSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Proposal
        fields = ['id', 'project', 'created_by', 'created_by_username', 'title', 'description',
                  'proposed_cost', 'status', 'created_at', 'sent_at', 'approved_at', 'rejected_at',
                  'expiry_date', 'revision_count', 'terms_conditions']
        read_only_fields = ['created_at', 'sent_at', 'approved_at', 'rejected_at']


class FeedbackSerializer(serializers.ModelSerializer):
    provided_by_username = serializers.CharField(source='provided_by.username', read_only=True)
    
    class Meta:
        model = Feedback
        fields = ['id', 'project', 'provided_by', 'provided_by_username', 'title', 'description',
                  'priority', 'is_resolved', 'resolved_at', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'resolved_at']
