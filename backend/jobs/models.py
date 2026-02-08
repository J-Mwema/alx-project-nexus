from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        OPEN = 'OPEN', 'Open'
        REVIEWED = 'REVIEWED', 'Reviewed'
        CLOSED = 'CLOSED', 'Closed'


    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        null=True,
        related_name='jobs'
    )
    job_type = models.ForeignKey(
        JobType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='jobs'
    )
    location = models.CharField(max_length=255)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['location']),
            models.Index(fields=['status']),
            models.Index(fields=['industry']),
            models.Index(fields=['job_type']),
        ]

    def __str__(self):
        return f"{self.title} ({self.status})"
