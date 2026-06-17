from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Message, Proposal, Feedback
from .serializers import MessageSerializer, ProposalSerializer, FeedbackSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """Message management - direct messaging and project discussions"""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['sender', 'receiver', 'project', 'is_read']
    ordering_fields = ['-created_at', '-updated_at']
    
    def get_queryset(self):
        """Users see only their messages"""
        user = self.request.user
        return Message.objects.filter(
            models.Q(sender=user) | models.Q(receiver=user)
        ).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
    
    @action(detail=False, methods=['patch'])
    def mark_as_read(self, request):
        """Mark messages as read"""
        Message.objects.filter(receiver=request.user, is_read=False).update(is_read=True)
        return Response({'status': 'marked_as_read'})


class ProposalViewSet(viewsets.ModelViewSet):
    """Proposal/Quote management"""
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'status', 'created_by']
    ordering_fields = ['-created_at', 'proposed_cost']
    
    def get_queryset(self):
        return Proposal.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def approve(self, request, pk=None):
        """Approve a proposal"""
        proposal = self.get_object()
        proposal.status = 'approved'
        proposal.approved_at = timezone.now()
        proposal.save()
        return Response({'status': 'proposal_approved'})
    
    @action(detail=True, methods=['patch'])
    def reject(self, request, pk=None):
        """Reject a proposal"""
        proposal = self.get_object()
        proposal.status = 'rejected'
        proposal.rejected_at = timezone.now()
        proposal.save()
        return Response({'status': 'proposal_rejected'})


class FeedbackViewSet(viewsets.ModelViewSet):
    """Feedback management on deliverables"""
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'priority', 'is_resolved']
    ordering_fields = ['-created_at', 'priority']
    
    def get_queryset(self):
        return Feedback.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(provided_by=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def resolve(self, request, pk=None):
        """Mark feedback as resolved"""
        feedback = self.get_object()
        feedback.is_resolved = True
        feedback.resolved_at = timezone.now()
        feedback.save()
        return Response({'status': 'feedback_resolved'})
