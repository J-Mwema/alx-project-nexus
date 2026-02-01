from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from users.models import User
from .models import Industry, JobType, Job


class JobAPITests(APITestCase):
    def setUp(self):
        self.employer = User.objects.create_user(username='emp', email='emp@example.com', password='pass1234', role=User.Role.EMPLOYER)
        self.jobseeker = User.objects.create_user(username='seek', email='seek@example.com', password='pass1234', role=User.Role.JOBSEEKER)
        self.ind = Industry.objects.create(name='Software')
        self.jt = JobType.objects.create(name='Full-time')

    def test_create_and_filter_job(self):
        self.client.force_authenticate(user=self.employer)
        url = reverse('job-list-create')
        data = {
            'title': 'Django Developer',
            'description': 'Work on backend',
            'industry_id': self.ind.id,
            'job_type_id': self.jt.id,
            'location': 'Remote',
            'status': 'OPEN'
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)

        # filter by industry
        resp = self.client.get(f"{url}?industry={self.ind.id}")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.data) >= 1)
