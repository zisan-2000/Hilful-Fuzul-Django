from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)   # /api/products/categories/
router.register(r'', ProductViewSet)             # /api/products/

urlpatterns = router.urls
