"""
URL configuration for config project.
"""
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from users.views import UserRegistrationView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Job Board API",
        default_version='v1',
        description="API documentation for Job Board backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', UserRegistrationView.as_view(), name="register"),


    path('api/jobs/', include('jobs.urls')),

    path('api/applications/', include('applications.urls')),

    # Swagger/OpenAPI
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
