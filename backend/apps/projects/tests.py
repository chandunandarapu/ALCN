from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

User = get_user_model()

class ProjectTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.client.force_authenticate(user=self.user)

    def test_project_list(self):

        response = self.client.get(
            "/api/projects/"
        )

        self.assertEqual(
            response.status_code,
            200
        )
