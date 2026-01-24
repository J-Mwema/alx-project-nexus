from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployer, IsJobOwner

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(status='OPEN')
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsEmployer()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsEmployer, IsJobOwner]
