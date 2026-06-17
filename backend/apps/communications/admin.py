from django.contrib import admin
from .models import Message, Proposal, Feedback


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['sender__username', 'receiver__username', 'content']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'proposed_cost', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'project__name']
    readonly_fields = ['created_at', 'sent_at', 'approved_at', 'rejected_at']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'priority', 'is_resolved', 'created_at']
    list_filter = ['priority', 'is_resolved', 'created_at']
    search_fields = ['title', 'project__name']
    readonly_fields = ['created_at', 'updated_at']
