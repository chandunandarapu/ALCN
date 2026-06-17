from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('payments/', include(router.urls)),
]
