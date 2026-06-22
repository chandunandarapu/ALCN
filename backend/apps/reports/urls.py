from django.urls import path

from .views import (
    ReportsHomeAPIView,
    ProjectReportAPIView,
    TaskReportAPIView,
    ClientReportAPIView,
    RevenueReportAPIView,
    ExportProjectsCSVAPIView,
    ExportTasksCSVAPIView,
    ExportClientsCSVAPIView,
)

urlpatterns = [
    path("", ReportsHomeAPIView.as_view()),
    path("projects/", ProjectReportAPIView.as_view()),
    path("tasks/", TaskReportAPIView.as_view()),
    path("clients/", ClientReportAPIView.as_view()),
    path("revenue/", RevenueReportAPIView.as_view()),
    path("export/projects/csv/", ExportProjectsCSVAPIView.as_view()),
    path("export/tasks/csv/", ExportTasksCSVAPIView.as_view()),
    path("export/clients/csv/", ExportClientsCSVAPIView.as_view()),
]