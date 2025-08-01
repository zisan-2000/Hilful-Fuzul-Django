from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'', BlogViewSet)  # /api/blog/

urlpatterns = router.urls
