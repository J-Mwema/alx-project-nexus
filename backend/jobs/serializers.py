from rest_framework import serializers
from .models import Job, Industry, JobType


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'name')


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id', 'name')


class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.username')

    industry = IndustrySerializer(read_only=True)
    industry_id = serializers.PrimaryKeyRelatedField(
        queryset=Industry.objects.all(), source='industry', write_only=True, required=False, allow_null=True
    )

    job_type = JobTypeSerializer(read_only=True)
    job_type_id = serializers.PrimaryKeyRelatedField(
        queryset=JobType.objects.all(), source='job_type', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('id', 'employer', 'created_at', 'updated_at')

