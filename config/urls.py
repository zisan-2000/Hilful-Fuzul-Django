from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/writers/', include('writers.urls')),
    path('api/publishers/', include('publishers.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/contact/', include('contact.urls')),
]
