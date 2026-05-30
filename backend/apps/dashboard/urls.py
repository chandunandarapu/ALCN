from django.urls import path

from .views import (
    MonthlyProjectsAPIView,
    MonthlyTasksAPIView,
    ProjectStatusAPIView,
    TaskStatusAPIView,
    OverdueTasksAPIView,
    HighPriorityTasksAPIView,
)

urlpatterns = [

    path(
        "monthly-projects/",
        MonthlyProjectsAPIView.as_view()
    ),

    path(
        "monthly-tasks/",
        MonthlyTasksAPIView.as_view()
    ),

    path(
        "project-status/",
        ProjectStatusAPIView.as_view()
    ),

    path(
        "task-status/",
        TaskStatusAPIView.as_view()
    ),

    path(
        "overdue-tasks/",
        OverdueTasksAPIView.as_view()
    ),

    path(
        "high-priority-tasks/",
        HighPriorityTasksAPIView.as_view()
    ),

]