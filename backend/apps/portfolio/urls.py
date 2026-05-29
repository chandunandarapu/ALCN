from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet

router = DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)

urlpatterns = router.urls