from django.test import TestCase
from rest_framework.test import APITestCase

class ProjectTestCase(APITestCase):

    def test_project_list(self):

        response = self.client.get(
            "/api/projects/"
        )

        self.assertEqual(
            response.status_code,
            200
        )