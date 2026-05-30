from datetime import date

from django.db.models import Count
from django.db.models.functions import ExtractMonth
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.projects.models import Project
from apps.tasks.models import Task


class MonthlyProjectsAPIView(APIView):

    def get(self, request):

        data = (
            Project.objects
            .annotate(month=ExtractMonth("created_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

        return Response(data)


class MonthlyTasksAPIView(APIView):

    def get(self, request):

        data = (
            Task.objects
            .annotate(month=ExtractMonth("created_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

        return Response(data)


class ProjectStatusAPIView(APIView):

    def get(self, request):

        data = {
            "pending": Project.objects.filter(status="pending").count(),
            "in_progress": Project.objects.filter(status="in_progress").count(),
            "completed": Project.objects.filter(status="completed").count(),
            "on_hold": Project.objects.filter(status="on_hold").count(),
        }

        return Response(data)


class TaskStatusAPIView(APIView):

    def get(self, request):

        data = {
            "todo": Task.objects.filter(status="todo").count(),
            "in_progress": Task.objects.filter(status="in_progress").count(),
            "completed": Task.objects.filter(status="completed").count(),
        }

        return Response(data)


class OverdueTasksAPIView(APIView):

    def get(self, request):

        tasks = Task.objects.filter(
            due_date__lt=date.today(),
            status__in=["todo", "in_progress"]
        ).values(
            "id",
            "title",
            "due_date",
            "priority"
        )

        return Response(tasks)


class HighPriorityTasksAPIView(APIView):

    def get(self, request):

        tasks = Task.objects.filter(
            priority="high"
        ).values(
            "id",
            "title",
            "status",
            "priority"
        )

        return Response(tasks)