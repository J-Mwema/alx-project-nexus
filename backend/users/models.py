from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user models to support RBAC
    """

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EMPLOYER = 'EMPLOYER', 'Employer'
        JOBSEEKER = 'JOBSEEKER', 'Job Seeker'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.JOBSEEKER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
