import csv
from decimal import Decimal
from io import StringIO

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.clients.models import Client
from apps.projects.models import Project
from apps.tasks.models import Task


class ReportsAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reporter",
            password="password123",
            role="admin",
        )
        self.client.force_authenticate(self.user)

        self.company = Client.objects.create(
            company_name="Acme Corp",
            contact_person="Jane Client",
            email="jane@example.com",
            phone="5551234567",
            status="active",
            created_by=self.user,
        )
        self.project = Project.objects.create(
            client=self.company,
            title="Website Build",
            status="completed",
            budget=Decimal("1250.50"),
            assigned_to=self.user,
        )
        Task.objects.create(
            project=self.project,
            title="Design homepage",
            status="todo",
            assigned_to=self.user,
        )

    def test_project_report_counts_and_revenue(self):
        project_response = self.client.get("/api/reports/projects/")
        revenue_response = self.client.get("/api/reports/revenue/")

        self.assertEqual(project_response.status_code, 200)
        self.assertEqual(project_response.data["total_projects"], 1)
        self.assertEqual(project_response.data["completed_projects"], 1)
        self.assertEqual(project_response.data["pending_projects"], 0)

        self.assertEqual(revenue_response.status_code, 200)
        self.assertEqual(revenue_response.data["total_revenue"], Decimal("1250.50"))

    def test_client_csv_export_uses_existing_client_fields(self):
        response = self.client.get("/api/reports/export/clients/csv/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")

        rows = list(csv.reader(StringIO(response.content.decode())))
        self.assertEqual(
            rows[0],
            ["ID", "Company Name", "Contact Person", "Email", "Created At"],
        )
        self.assertEqual(rows[1][1:4], ["Acme Corp", "Jane Client", "jane@example.com"])
