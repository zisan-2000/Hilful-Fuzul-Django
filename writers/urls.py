from rest_framework.routers import DefaultRouter
from .views import WriterViewSet

router = DefaultRouter()
router.register(r'', WriterViewSet)  # /api/writers/

urlpatterns = router.urls
