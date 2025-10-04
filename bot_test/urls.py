from django.contrib import admin
from django.urls import path, include

#from home.views import hindex
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter
from home.views import CourseViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
   # path('', hindex),
    path('admin/', admin.site.urls),

    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
