from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone

from .models import Invoice, Transaction
from .serializers import InvoiceSerializer, TransactionSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """Invoice management"""
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'status', 'payment_method']
    ordering_fields = ['-created_at', 'due_date']
    
    def get_queryset(self):
        return Invoice.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def send(self, request, pk=None):
        """Mark invoice as sent"""
        invoice = self.get_object()
        invoice.status = 'sent'
        invoice.sent_date = timezone.now()
        invoice.save()
        return Response({'status': 'invoice_sent'})
    
    @action(detail=True, methods=['patch'])
    def mark_paid(self, request, pk=None):
        """Mark invoice as paid"""
        invoice = self.get_object()
        invoice.status = 'paid'
        invoice.paid_date = timezone.now()
        invoice.save()
        return Response({'status': 'invoice_marked_paid'})


class TransactionViewSet(viewsets.ModelViewSet):
    """Payment transaction management"""
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['invoice', 'status', 'payment_gateway']
    ordering_fields = ['-created_at']
    
    def get_queryset(self):
        return Transaction.objects.all()
