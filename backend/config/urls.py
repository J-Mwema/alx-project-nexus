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



urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', UserRegistrationView.as_view(), name="register"),


    path('api/jobs', include('jobs.urls')),
]
