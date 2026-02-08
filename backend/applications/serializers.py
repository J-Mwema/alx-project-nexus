from rest_framework import serializers
from .models import Application

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'job', 'cover_letter')
        read_only_fields = ('id',)

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            job = attrs.get('job')
            if Application.objects.filter(applicant=request.user, job=job).exists():
                raise serializers.ValidationError("You have already applied for this job.")
        return attrs

class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('status',)
