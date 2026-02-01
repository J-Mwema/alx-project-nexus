from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from jobs.models import Job, Industry, JobType


class ApplicationAPITests(APITestCase):
    def setUp(self):
        self.employer = User.objects.create_user(username='emp', email='emp@example.com', password='pass1234', role=User.Role.EMPLOYER)
        self.jobseeker = User.objects.create_user(username='seek', email='seek@example.com', password='pass1234', role=User.Role.JOBSEEKER)
        self.ind = Industry.objects.create(name='Software')
        self.jt = JobType.objects.create(name='Full-time')
        self.job = Job.objects.create(
            employer=self.employer,
            title='Django Dev',
            description='Backend work',
            industry=self.ind,
            job_type=self.jt,
            location='Remote',
            status='OPEN'
        )

    def test_apply_and_unique_constraint(self):
        self.client.force_authenticate(user=self.jobseeker)
        url = reverse('apply-job')
        data = {'job': self.job.id, 'cover_letter': 'please hire me'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)

        # applying again should fail due to unique_together
        resp2 = self.client.post(url, data, format='json')
        self.assertNotEqual(resp2.status_code, 201)
