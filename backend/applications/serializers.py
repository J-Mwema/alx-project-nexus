from rest_framework import serializers
from .models import Application

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'job', 'cover_letter')
        read_only_fields = ('id',)

class ApplicatioinStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('status',)
