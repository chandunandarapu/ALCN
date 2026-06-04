from django.urls import path

from .views import (
    DashboardHomeAPIView,
    MonthlyProjectsAPIView,
    MonthlyTasksAPIView,
    ProjectStatusAPIView,
    TaskStatusAPIView,
    OverdueTasksAPIView,
    HighPriorityTasksAPIView,
)

urlpatterns = [

    # Dashboard Home
    path(
        "",
        DashboardHomeAPIView.as_view(),
        name="dashboard-home"
    ),

    # Monthly Projects
    path(
        "monthly-projects/",
        MonthlyProjectsAPIView.as_view(),
        name="monthly-projects"
    ),

    # Monthly Tasks
    path(
        "monthly-tasks/",
        MonthlyTasksAPIView.as_view(),
        name="monthly-tasks"
    ),

    # Project Status Report
    path(
        "project-status/",
        ProjectStatusAPIView.as_view(),
        name="project-status"
    ),

    # Task Status Report
    path(
        "task-status/",
        TaskStatusAPIView.as_view(),
        name="task-status"
    ),

    # Overdue Tasks
    path(
        "overdue-tasks/",
        OverdueTasksAPIView.as_view(),
        name="overdue-tasks"
    ),

    # High Priority Tasks
    path(
        "high-priority-tasks/",
        HighPriorityTasksAPIView.as_view(),
        name="high-priority-tasks"
    ),
]