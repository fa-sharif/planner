from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from projects.models import Project

class ProjectTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.project = Project.objects.create(name='Test Project', owner=self.user)

    def test_create_project(self):
        url = reverse('project-list')
        data = {'name': 'New Project'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_projects(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_project(self):
        url = reverse('project-detail', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        url = reverse('project-detail', args=[self.project.id])
        data = {'name': 'Updated Project'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, 'Updated Project')

    def test_delete_project(self):
        url = reverse('project-detail', args=[self.project.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
