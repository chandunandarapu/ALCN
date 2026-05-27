from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "client",
        "status",
        "budget",
        "deadline",
        "assigned_to",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "title",
        "client__company_name",
    )

    ordering = ("-created_at",)