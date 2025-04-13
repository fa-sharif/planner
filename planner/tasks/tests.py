from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import CustomUser
from projects.models import Project
from tasks.models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        self.project = Project.objects.create(name="Test Project", owner=self.user)
        self.task_data = {
            "title": "Test Task",
            "description": "A sample task",
            "project": self.project.id,
            "status": "todo",
            "priority": "medium"
        }

    def test_create_task(self):
        url = reverse('task-list')
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, "Test Task")

    def test_list_tasks(self):
        Task.objects.create(title="T1", project=self.project)
        Task.objects.create(title="T2", project=self.project)

        url = reverse('task-list') # /api/tasks/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        task = Task.objects.create(title="Retrieve Me", project=self.project)
        url = reverse('task-detail', args=[task.id]) # /api/tasks/{id}
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Retrieve Me")

    def test_update_task(self):
        task = Task.objects.create(title="Old Title", project=self.project)
        url = reverse('task-detail', args=[task.id]) # /api/tasks/{id}
        updated_data = self.task_data.copy()
        updated_data["title"] = "Updated Title"
        updated_data["project"] = self.project.id

        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Title")

    def test_delete_task(self):
        task = Task.objects.create(title="Delete Me", project=self.project)
        url = reverse('task-detail', args=[task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
