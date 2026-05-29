from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer

    # permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ['status']
    search_fields = [
        'company_name',
        'contact_person',
        'email',
        'phone'
    ]
    ordering_fields = [
        'company_name',
        'contact_person',
        'status'
    ]