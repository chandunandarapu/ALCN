from django.contrib import admin
from .models import Invoice, Transaction


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'project', 'total_amount', 'status', 'due_date']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['invoice_number', 'project__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'invoice', 'amount', 'status', 'payment_gateway']
    list_filter = ['status', 'payment_gateway', 'created_at']
    search_fields = ['transaction_id', 'invoice__invoice_number']
    readonly_fields = ['created_at', 'updated_at']
