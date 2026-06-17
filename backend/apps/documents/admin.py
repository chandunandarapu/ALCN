from django.contrib import admin
from .models import Document, DocumentVersion


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'document_type', 'version', 'is_public', 'created_at']
    list_filter = ['document_type', 'is_public', 'is_final', 'created_at']
    search_fields = ['title', 'project__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(DocumentVersion)
class DocumentVersionAdmin(admin.ModelAdmin):
    list_display = ['document', 'version_number', 'changed_by', 'created_at']
    list_filter = ['created_at']
    search_fields = ['document__title']
    readonly_fields = ['created_at']
