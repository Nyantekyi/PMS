from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']
    
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id = self.request.query_params.get('project', None)
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        assignee = self.request.query_params.get('assignee', None)
        
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if assignee:
            queryset = queryset.filter(assignee_id=assignee)
        
        return queryset

