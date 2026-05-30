from rest_framework import serializers

from .models import Project
from apps.clients.serializers import ClientSerializer
from apps.users.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):

    client = ClientSerializer(read_only=True)

    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'