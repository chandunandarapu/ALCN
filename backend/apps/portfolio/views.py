from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('id')
    serializer_class = PortfolioSerializer

    # permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        'created_at',
    ]

    search_fields = [
        'title',
        'description',
    ]

    ordering_fields = [
        'title',
        'created_at',
    ]