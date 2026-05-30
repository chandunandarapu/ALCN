from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ProjectViewSet,
    SendEmailAPIView
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls + [
    path(
        'send-email/',
        SendEmailAPIView.as_view(),
        name='send-email'
    ),
]