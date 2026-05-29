from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'client']
    
    search_fields = [
    'title',
    'description'
    ]