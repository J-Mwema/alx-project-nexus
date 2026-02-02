from django.contrib import admin
from .models import Job, Industry, JobType


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'employer', 'status', 'industry', 'job_type', 'created_at')
    list_filter = ('status', 'industry', 'job_type', 'location')
    search_fields = ('title', 'description', 'location')
    raw_id_fields = ('employer',)
