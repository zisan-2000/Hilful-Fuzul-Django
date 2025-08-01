from rest_framework.routers import DefaultRouter
from .views import PublisherViewSet

router = DefaultRouter()
router.register(r'', PublisherViewSet)  # /api/publishers/

urlpatterns = router.urls
