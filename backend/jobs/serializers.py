from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.username')

    class Meta:
        model = Job
        read_only_fields = ('id', 'employer', 'created_at', 'updated_at')

