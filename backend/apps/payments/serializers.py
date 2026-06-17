from rest_framework import serializers
from .models import Invoice, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'invoice', 'amount', 'status', 'payment_gateway', 'transaction_id', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class InvoiceSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Invoice
        fields = ['id', 'project', 'created_by', 'created_by_username', 'invoice_number', 'amount',
                  'tax_amount', 'total_amount', 'description', 'status', 'issued_date', 'due_date',
                  'sent_date', 'paid_date', 'payment_method', 'transactions', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'issued_date']
