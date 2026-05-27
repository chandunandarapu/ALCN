from django.db import models
from django.conf import settings


class Client(models.Model):

    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("lead", "Lead"),
    )

    company_name = models.CharField(max_length=255)

    contact_person = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    address = models.TextField(blank=True, null=True)

    website = models.URLField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="lead"
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="clients"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name