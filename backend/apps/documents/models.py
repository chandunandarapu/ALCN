from django.db import models
from django.core.validators import FileExtensionValidator
from apps.users.models import User
from apps.projects.models import Project


class Document(models.Model):
    """File management for projects"""
    DOCUMENT_TYPE_CHOICES = [
        ('proposal', 'Proposal'),
        ('contract', 'Contract'),
        ('deliverable', 'Deliverable'),
        ('resource', 'Resource'),
        ('report', 'Report'),
        ('other', 'Other'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_documents')
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.BigIntegerField(help_text="File size in bytes")
    
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES, default='other')
    version = models.IntegerField(default=1)
    
    is_public = models.BooleanField(default=False, help_text="Visible to client")
    is_final = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['project', '-created_at']),
            models.Index(fields=['document_type']),
        ]
    
    def __str__(self):
        return f"{self.title} (v{self.version})"


class DocumentVersion(models.Model):
    """Version history for documents"""
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='versions')
    
    version_number = models.IntegerField()
    file = models.FileField(upload_to='documents/versions/%Y/%m/%d/')
    
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    change_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('document', 'version_number')
        ordering = ['-version_number']
    
    def __str__(self):
        return f"{self.document.title} - v{self.version_number}"
