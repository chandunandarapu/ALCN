import csv
import pandas as pd
from io import BytesIO
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.clients.models import Client
from apps.projects.models import Project
from apps.tasks.models import Task

from rest_framework.views import APIView
from rest_framework.response import Response

class ReportsHomeAPIView(APIView):

    def get(self, request):
        return Response({
            "projects": "/api/reports/projects/",
            "tasks": "/api/reports/tasks/",
            "clients": "/api/reports/clients/",
            "revenue": "/api/reports/revenue/",
            "project_csv": "/api/reports/export/projects/csv/",
            "project_excel": "/api/reports/export/projects/excel/",
        })


class ProjectReportAPIView(APIView):

    def get(self, request):
        data = {
            "total_projects": Project.objects.count(),
            "completed_projects": Project.objects.filter(
                status="completed"
            ).count(),
            "pending_projects": Project.objects.filter(
                status="pending"
            ).count(),
        }
        return Response(data)


class TaskReportAPIView(APIView):

    def get(self, request):
        data = {
            "total_tasks": Task.objects.count(),
            "completed_tasks": Task.objects.filter(
                status="completed"
            ).count(),
            "pending_tasks": Task.objects.filter(
                status="todo"
            ).count(),
        }
        return Response(data)


class ClientReportAPIView(APIView):

    def get(self, request):
        return Response({
            "total_clients": Client.objects.count()
        })


class RevenueReportAPIView(APIView):

    def get(self, request):
        revenue = sum(
            project.budget or 0
            for project in Project.objects.all()
        )

        return Response({
            "total_revenue": revenue
        })


class ExportProjectsCSVAPIView(APIView):

    def get(self, request):

        response = HttpResponse(content_type='text/csv')

        response['Content-Disposition'] = (
            'attachment; filename="projects.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            'ID',
            'Title',
            'Status',
            'Budget',
            'Created At'
        ])

        projects = Project.objects.all()

        for project in projects:
            writer.writerow([
                project.id,
                project.title,
                project.status,
                project.budget,
                project.created_at
            ])

        return response
    
class ExportTasksCSVAPIView(APIView):

    def get(self, request):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename="tasks.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            'ID',
            'Title',
            'Status',
            'Created At'
        ])

        tasks = Task.objects.all()

        for task in tasks:
            writer.writerow([
                task.id,
                task.title,
                task.status,
                task.created_at
            ])

        return response


class ExportClientsCSVAPIView(APIView):

    def get(self, request):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename="clients.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            'ID',
            'Name',
            'Email',
            'Created At'
        ])

        clients = Client.objects.all()

        for client in clients:
            writer.writerow([
                client.id,
                client.name,
                client.email,
                client.created_at
            ])

        return response
    

class ExportProjectsExcelAPIView(APIView):

    def get(self, request):

        projects = Project.objects.all()

        data = []

        for project in projects:
            data.append({
                "ID": project.id,
                "Title": project.title,
                "Status": project.status,
                "Budget": project.budget,
                "Created At": project.created_at.replace(tzinfo=None) 
                if project.created_at else None
            })

        df = pd.DataFrame(data)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = (
            'attachment; filename="projects.xlsx"'
        )

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

        return response
    
class ExportTasksExcelAPIView(APIView):

    def get(self, request):

        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "ID": task.id,
                "Title": task.title,
                "Status": task.status,
                "Created At": task.created_at.replace(tzinfo=None)
                if task.created_at else None
            })

        df = pd.DataFrame(data)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = (
            'attachment; filename="tasks.xlsx"'
        )

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

        return response
    

class ExportClientsExcelAPIView(APIView):

    def get(self, request):

        clients = Client.objects.all()

        data = []

        for client in clients:
            data.append({
                "ID": client.id,
                "Name": client.name,
                "Email": client.email,
                "Created At": client.created_at.replace(tzinfo=None)
                if client.created_at else None,
            })

        df = pd.DataFrame(data)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response['Content-Disposition'] = (
            'attachment; filename="clients.xlsx"'
        )

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

        return response