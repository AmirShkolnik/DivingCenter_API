from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test comment')
        self.assertEqual(self.comment.owner, self.user)
        self.assertEqual(self.comment.post, self.post)

    def test_comment_str_method(self):
        self.assertEqual(str(self.comment), 'Test comment')

class CommentSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        self.factory = APIRequestFactory()
        request = self.factory.get('/')
        request.user = self.user
        self.serializer = CommentSerializer(instance=self.comment, context={'request': request})

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                                            'post', 'created_at', 'updated_at', 'content'])

class CommentViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(owner=self.user, content='Test post')
        self.comment = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content='Test comment'
        )
        self.client.force_authenticate(user=self.user)

    def test_comment_list_view(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_create_view(self):
        data = {
            'post': self.post.id,
            'content': 'New test comment'
        }
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_detail_view(self):
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_update_view(self):
        data = {'content': 'Updated test comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated test comment')

    def test_comment_delete_view(self):
        response = self.client.delete(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_unauthorized_comment_create(self):
        self.client.logout()
        data = {
            'post': self.post.id,
            'content': 'Unauthorized comment'
        }
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_comment_update(self):
        self.client.logout()
        data = {'content': 'Unauthorized update'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_comment_delete(self):
        self.client.logout()
        response = self.client.delete(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)