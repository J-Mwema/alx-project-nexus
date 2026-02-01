from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Industry, JobType
from .serializers import (
    JobSerializer,
    IndustrySerializer,
    JobTypeSerializer,
)
from .permissions import IsEmployer, IsJobOwner


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(status='OPEN').select_related('employer', 'industry', 'job_type')
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['industry', 'job_type', 'location', 'status']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['created_at', 'updated_at', 'title']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsEmployer()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all().select_related('employer', 'industry', 'job_type')
    serializer_class = JobSerializer
    permission_classes = [IsEmployer, IsJobOwner]


class IndustryListCreateView(generics.ListCreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.AllowAny]


class JobTypeListCreateView(generics.ListCreateAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = [permissions.AllowAny]
