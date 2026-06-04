from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ['role', 'is_active']
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'date_joined']

    def get_permissions(self):
        """Allow unauthenticated POST (registration), require auth for others."""
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]