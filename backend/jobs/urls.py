from django.urls import path
from .views import JobListCreateView, JobDetailView

urlpatterns = [
        path('', JobListCreateView.as_view(), name='job-List-create'),
        path('<int:pk./', JobDetailView.as_view(), name='job-detail'),
]
