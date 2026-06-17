from django.db import models
from apps.users.models import User


class Notification(models.Model):
    """User notifications"""
    NOTIFICATION_TYPES = [
        ('message', 'New Message'),
        ('proposal', 'Proposal Update'),
        ('invoice', 'Invoice Alert'),
        ('project', 'Project Update'),
        ('payment', 'Payment Confirmation'),
        ('document', 'Document Upload'),
        ('system', 'System Notification'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    action_url = models.CharField(max_length=255, blank=True)
    related_object_id = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['user', 'is_read']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"


class EmailLog(models.Model):
    """Log of sent emails"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('bounced', 'Bounced'),
    ]
    
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    email_type = models.CharField(max_length=50)  # welcome, invoice, proposal, etc
    related_object_id = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', '-created_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"Email to {self.recipient} - {self.subject}"
