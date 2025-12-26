from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from projects.serializers import ProjectSerializer, UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    assignee_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'project_id', 
                  'assignee', 'assignee_id', 'priority', 'status', 'due_date', 
                  'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
