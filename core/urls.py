from apps.views import  CarViewSet
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
router = DefaultRouter()
router.register('cars', CarViewSet, basename='cars')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('api/', include(router.urls)),
    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)