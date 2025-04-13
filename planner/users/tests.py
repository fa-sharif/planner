from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class UserTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser(username="admin", password="adminpass", email="admin@example.com")
        self.normal_user = CustomUser.objects.create_user(username="user1", password="userpass", email="user1@example.com")

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_register_user(self):
        url = reverse('user-list-create')  # ➜ /api/user/create

        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.filter(username='newuser').exists(), True)

    def test_user_cannot_list_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token(self.normal_user)}')
        url = reverse('user-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_list_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_token(self.admin_user)}')
        url = reverse('user-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_view_and_update_own_profile(self):
        token = self.get_token(self.normal_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.normal_user.username)

        # Update email
        updated_data = {
            'username': 'user1',
            'email': 'newemail@example.com'
        }
        response = self.client.patch(url, updated_data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.normal_user.refresh_from_db()
        self.assertEqual(self.normal_user.email, 'newemail@example.com')
