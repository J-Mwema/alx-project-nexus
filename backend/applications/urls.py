from django.urls import path
from .views import (
        ApplicationCreateView,
        ApplicationStatusUpdateView,
)

urlpatterns = [
    path('', ApplicationCreateView.as_view(), name='apply-job'),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view(), name='update-application-status'),
]
