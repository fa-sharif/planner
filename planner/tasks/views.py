# from rest_framework import viewsets, permissions
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Task.objects.filter(project__owner=self.request.user)

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save()
        self.send_ws_notification(task,created=True)

    def perform_update(self, serializer):
        task = serializer.save()
        self.send_ws_notification(task,created=False)
        
    def send_ws_notification(self, task, created):
        channel_layer = get_channel_layer()
        data = {
            "type": "task_notification",
            "data": {
                "message": f"Task {'created' if created else 'updated'}: {task.title}",
                "task_id": task.id,
            },
        }
        group_name = f"user_{task.assignee.id}"  # فقط به مسئول اون تسک پیام بده
        async_to_sync(channel_layer.group_send)(group_name, data)


