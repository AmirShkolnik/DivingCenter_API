from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Follower
from .serializers import FollowerSerializer


class FollowerModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', password='pass1234'
        )
        self.user2 = User.objects.create_user(
            username='user2', password='pass1234'
        )

    def test_follower_creation(self):
        follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )
        self.assertEqual(str(follower), f'{self.user1} {self.user2}')

    def test_unique_together_constraint(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        with self.assertRaises(Exception):
            Follower.objects.create(owner=self.user1, followed=self.user2)


class FollowerSerializerTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', password='pass1234'
        )
        self.user2 = User.objects.create_user(
            username='user2', password='pass1234'
        )
        self.follower_data = {
            'owner': self.user1,
            'followed': self.user2.id
        }
        self.serializer = FollowerSerializer(data=self.follower_data)

    def test_serializer_with_valid_data(self):
        self.assertTrue(self.serializer.is_valid())


class FollowerViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='user1', password='pass1234'
        )
        self.user2 = User.objects.create_user(
            username='user2', password='pass1234'
        )
        self.client.force_authenticate(user=self.user1)

    def test_create_follower(self):
        response = self.client.post(
            '/followers/', {'followed': self.user2.id}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_follower(self):
        Follower.objects.create(owner=self.user1, followed=self.user2)
        response = self.client.post(
            '/followers/', {'followed': self.user2.id}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("Response data:", response.data)
        self.assertIn('detail', response.data)
        self.assertIn(
            'You are already following this user',
            str(response.data['detail'])
        )

    def test_list_followers(self):
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_follower(self):
        follower = Follower.objects.create(
            owner=self.user1, followed=self.user2
        )
        response = self.client.delete(f'/followers/{follower.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
