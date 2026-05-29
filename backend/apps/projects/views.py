from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

    # permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        'status',
        'client',
        'assigned_to',
    ]

    search_fields = [
        'title',
        'description',
        'client__company_name',
    ]

    ordering_fields = [
        'title',
        'budget',
        'start_date',
        'deadline',
        'created_at',
    ]