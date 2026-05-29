from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer

from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    
    search_fields = [
    'company_name',
    'contact_person',
    'email'
]