from django.db import models
from apps.users.models import User
from apps.projects.models import Project


class Message(models.Model):
    """Direct or project-based messaging"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    
    subject = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['receiver', '-created_at']),
            models.Index(fields=['sender', '-created_at']),
        ]
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"


class Proposal(models.Model):
    """Quotes and service proposals"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent to Client'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='proposal')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_proposals')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    proposed_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    
    expiry_date = models.DateField(null=True, blank=True)
    revision_count = models.IntegerField(default=0)
    
    terms_conditions = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Proposal - {self.title} (₹{self.proposed_cost})"


class Feedback(models.Model):
    """Client feedback on deliverables"""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedback')
    provided_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='provided_feedback')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Feedback - {self.title}"
