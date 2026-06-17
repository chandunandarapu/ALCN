from rest_framework import serializers
from .models import Document, DocumentVersion


class DocumentVersionSerializer(serializers.ModelSerializer):
    changed_by_username = serializers.CharField(source='changed_by.username', read_only=True)
    
    class Meta:
        model = DocumentVersion
        fields = ['id', 'version_number', 'file', 'changed_by', 'changed_by_username', 'change_notes', 'created_at']
        read_only_fields = ['created_at']


class DocumentSerializer(serializers.ModelSerializer):
    uploaded_by_username = serializers.CharField(source='uploaded_by.username', read_only=True)
    versions = DocumentVersionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Document
        fields = ['id', 'project', 'uploaded_by', 'uploaded_by_username', 'title', 'description',
                  'file', 'file_type', 'file_size', 'document_type', 'version', 'is_public',
                  'is_final', 'versions', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'file_type', 'file_size', 'versions']
