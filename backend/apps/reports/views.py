import csv

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clients.models import Client
from apps.projects.models import Project
from apps.tasks.models import Task


class ReportsHomeAPIView(APIView):
    def get(self, request):
        return Response({
            "projects": "/api/reports/projects/",
            "tasks": "/api/reports/tasks/",
            "clients": "/api/reports/clients/",
            "revenue": "/api/reports/revenue/",
            "project_csv": "/api/reports/export/projects/csv/",
            "task_csv": "/api/reports/export/tasks/csv/",
            "client_csv": "/api/reports/export/clients/csv/",
        })


class ProjectReportAPIView(APIView):
    def get(self, request):
        return Response({
            "total_projects": Project.objects.count(),
            "completed_projects": Project.objects.filter(
                status="completed"
            ).count(),
            "pending_projects": Project.objects.filter(
                status="pending"
            ).count(),
        })


class TaskReportAPIView(APIView):
    def get(self, request):
        return Response({
            "total_tasks": Task.objects.count(),
            "completed_tasks": Task.objects.filter(
                status="completed"
            ).count(),
            "pending_tasks": Task.objects.filter(
                status="todo"
            ).count(),
        })


class ClientReportAPIView(APIView):
    def get(self, request):
        return Response({
            "total_clients": Client.objects.count()
        })


class RevenueReportAPIView(APIView):
    def get(self, request):
        total_revenue = sum(
            project.budget or 0
            for project in Project.objects.all()
        )

        return Response({
            "total_revenue": total_revenue
        })


class ExportProjectsCSVAPIView(APIView):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="projects.csv"'
        )

        writer = csv.writer(response)
        writer.writerow([
            "ID",
            "Title",
            "Status",
            "Budget",
            "Created At",
        ])

        for project in Project.objects.all():
            writer.writerow([
                project.id,
                project.title,
                project.status,
                project.budget,
                project.created_at,
            ])

        return response


class ExportTasksCSVAPIView(APIView):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="tasks.csv"'
        )

        writer = csv.writer(response)
        writer.writerow([
            "ID",
            "Title",
            "Status",
            "Created At",
        ])

        for task in Task.objects.all():
            writer.writerow([
                task.id,
                task.title,
                task.status,
                task.created_at,
            ])

        return response


class ExportClientsCSVAPIView(APIView):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            'attachment; filename="clients.csv"'
        )

        writer = csv.writer(response)
        writer.writerow([
            "ID",
            "Company Name",
            "Contact Person",
            "Email",
            "Created At",
        ])

        for client in Client.objects.all():
            writer.writerow([
                client.id,
                client.company_name,
                client.contact_person,
                client.email,
                client.created_at,
            ])

        return response
