from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):

    total_users = serializers.IntegerField()

    total_clients = serializers.IntegerField()

    active_clients = serializers.IntegerField()

    total_projects = serializers.IntegerField()

    completed_projects = serializers.IntegerField()

    total_tasks = serializers.IntegerField()

    completed_tasks = serializers.IntegerField()

    high_priority_tasks = serializers.IntegerField()

    revenue = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    completed_projects_percentage = serializers.FloatField()