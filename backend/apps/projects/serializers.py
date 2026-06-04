from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Project
from apps.clients.models import Client
from apps.clients.serializers import ClientSerializer
from apps.users.serializers import UserSerializer

User = get_user_model()

class ProjectSerializer(serializers.ModelSerializer):

    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True
    )

    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = Project
        fields = '__all__'
