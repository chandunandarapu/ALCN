from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ProposalViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'proposals', ProposalViewSet, basename='proposal')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('communications/', include(router.urls)),
]
