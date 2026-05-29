from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    # permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = [
        'status',
        'priority',
        'project',
        'assigned_to',
    ]

    search_fields = [
        'title',
        'description',
        'project__title',
    ]

    ordering_fields = [
        'title',
        'priority',
        'due_date',
        'created_at',
    ]