from rest_framework import generics, permissions
from .models import Application
from .serializers import (
    ApplicationCreateSerializer,
    ApplicationStatusUpdateSerializer,
)
from .permissions import IsEmployerAndJobOwner
from users.models import User

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes = [IsEmployerAndJobOwner]
