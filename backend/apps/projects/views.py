from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer
from .tasks import send_project_email


class SendEmailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        send_project_email.delay()

        return Response({
            "message": "Email task started"
        })


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related(
        'client',
        'assigned_to'
    ).order_by('id')

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

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

    def get_permissions(self):
        """Allow unauthenticated GET (list/retrieve), require auth for writes."""
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        print("=" * 50)
        print("USER:", request.user)
        print("AUTH:", request.auth)
        print("=" * 50)

        return super().list(request, *args, **kwargs)