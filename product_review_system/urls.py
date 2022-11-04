from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from reviews import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='Product')
router.register(r'image', views.ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
]

# NOTE : THIS IS FOR UPLOAD IMAGE FILE

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
