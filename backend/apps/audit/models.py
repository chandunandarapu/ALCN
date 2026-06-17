from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.users.models import User


class ActivityLog(models.Model):
    """Activity logging for compliance and auditing"""
    ACTION_CHOICES = [
        ('create', 'Created'),
        ('update', 'Updated'),
        ('delete', 'Deleted'),
        ('view', 'Viewed'),
        ('download', 'Downloaded'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
        ('paid', 'Marked as Paid'),
        ('login', 'Login'),
        ('logout', 'Logout'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='activity_logs')
    
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    action_description = models.CharField(max_length=500)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.IntegerField(null=True, blank=True)
    object_name = models.CharField(max_length=255, blank=True)
    
    old_value = models.TextField(blank=True)
    new_value = models.TextField(blank=True)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['action']),
            models.Index(fields=['content_type', 'object_id']),
        ]
    
    def __str__(self):
        return f"{self.user} - {self.action} - {self.object_name}"
