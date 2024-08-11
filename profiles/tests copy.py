from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile

class ProfileAPITests(TestCase):

    def setUp(self):
        """Set up test users and profiles."""
        self.client = APIClient()

        # Create a user and profile
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = self.user.profile

        # Create another user and profile
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        self.other_profile = self.other_user.profile

    def authenticate(self, user):
        """Authenticate the client with the given user."""
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_profile_list(self):
        """Test retrieving the list of profiles."""
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)

    def test_profile_detail(self):
        """Test retrieving a single profile."""
        response = self.client.get(f'/profiles/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], self.user.username)

    def test_profile_update(self):
        """Test updating a profile."""
        self.authenticate(self.user)
        response = self.client.put(
            f'/profiles/{self.profile.id}/',
            {'name': 'Updated Name', 'content': 'Updated content.'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.name, 'Updated Name')
        self.assertEqual(self.profile.content, 'Updated content.')

    def test_profile_delete(self):
        """Test deleting a profile."""
        self.authenticate(self.user)
        response = self.client.delete(f'/profiles/{self.profile.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(id=self.profile.id)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)

    def test_profile_delete_not_owner(self):
        """Test that a user cannot delete another user's profile."""
        self.authenticate(self.other_user)
        response = self.client.delete(f'/profiles/{self.profile.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
