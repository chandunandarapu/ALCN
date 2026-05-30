from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_project_email


class SendEmailAPIView(APIView):

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