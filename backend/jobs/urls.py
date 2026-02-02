from django.urls import path
from .views import (
    JobListCreateView,
    JobDetailView,
    IndustryListCreateView,
    JobTypeListCreateView,
)

urlpatterns = [
    path('', JobListCreateView.as_view(), name='job-list-create'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('industries/', IndustryListCreateView.as_view(), name='industry-list-create'),
    path('job-types/', JobTypeListCreateView.as_view(), name='jobtype-list-create'),
]
