from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ActivityLog
from .serializers import ActivityLogSerializer


class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Activity logging (admin & compliance)"""
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['user', 'action', 'content_type']
    ordering_fields = ['-created_at']
    search_fields = ['user__username', 'action_description', 'object_name']
    
    def get_queryset(self):
        return ActivityLog.objects.all()
    
    @action(detail=False, methods=['get'])
    def user_activities(self, request):
        """Get activities for a specific user"""
        username = request.query_params.get('username')
        if username:
            logs = ActivityLog.objects.filter(user__username=username)
            serializer = self.get_serializer(logs, many=True)
            return Response(serializer.data)
        return Response({'error': 'username parameter required'})
    
    @action(detail=False, methods=['get'])
    def recent_activities(self, request):
        """Get recent activities across system"""
        limit = request.query_params.get('limit', 50)
        logs = ActivityLog.objects.all()[:int(limit)]
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)
