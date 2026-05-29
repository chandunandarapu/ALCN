from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['technology']
    
    search_fields = [
    'title',
    'description',
    'technology'
    ]