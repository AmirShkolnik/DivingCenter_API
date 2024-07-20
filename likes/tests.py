from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Like
from posts.models import Post


class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.like = Like.objects.create(owner=self.user, post=self.post)

    def test_like_creation(self):
        self.assertTrue(isinstance(self.like, Like))
        self.assertEqual(self.like.__str__(), f'{self.user} {self.post}')

    def test_like_unique_together(self):
        with self.assertRaises(Exception):
            Like.objects.create(owner=self.user, post=self.post)


class LikeSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_like_serializer_create(self):
        data = {'post': self.post.id}
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_serializer_duplicate(self):
        Like.objects.create(owner=self.user, post=self.post)
        data = {'post': self.post.id}
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LikeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_like_list_view(self):
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_create_view(self):
        data = {'post': self.post.id}
        response = self.client.post('/likes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_detail_view(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        response = self.client.get(f'/likes/{like.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_delete_view(self):
        like = Like.objects.create(owner=self.user, post=self.post)
        response = self.client.delete(f'/likes/{like.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
