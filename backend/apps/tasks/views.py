from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'priority']
    
    
    search_fields = [
    'title',
    'description'
    ]