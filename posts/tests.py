from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class PostListViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='adam', password='pass')
        self.url = reverse('post-list')
    
    def authenticate(self):
        self.client.login(username='adam', password='pass')
        self.client.force_authenticate(user=self.user)

    def test_can_list_posts(self):
        print("Testing list posts")
        Post.objects.create(owner=self.user, title='a title', content='some content')
        response = self.client.get(self.url)
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'a title')

    def test_logged_in_user_can_create_post(self):
        print("Testing logged in user can create post")
        self.authenticate()
        response = self.client.post(self.url, {'title': 'a title', 'content': 'some content'})
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'a title')

    def test_user_not_logged_in_cant_create_post(self):
        print("Testing user not logged in can't create post")
        response = self.client.post(self.url, {'title': 'a title', 'content': 'some content'})
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(username='brian', password='pass')
        self.adam_post = Post.objects.create(owner=self.adam, title='a title', content='adams content')
        self.brian_post = Post.objects.create(owner=self.brian, title='another title', content='brians content')
        self.detail_url_adam = reverse('post-detail', kwargs={'pk': self.adam_post.pk})
        self.detail_url_brian = reverse('post-detail', kwargs={'pk': self.brian_post.pk})
    
    def authenticate(self, user):
        self.client.login(username=user.username, password='pass')
        self.client.force_authenticate(user=user)

    def test_can_retrieve_post_using_valid_id(self):
        print("Testing retrieve post using valid id")
        response = self.client.get(self.detail_url_adam)
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'a title')

    def test_cant_retrieve_post_using_invalid_id(self):
        print("Testing retrieve post using invalid id")
        invalid_url = reverse('post-detail', kwargs={'pk': 999})
        response = self.client.get(invalid_url)
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        print("Testing user can update own post")
        self.authenticate(self.adam)
        response = self.client.put(self.detail_url_adam, {'title': 'a new title', 'content': 'updated content'})
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.adam_post.refresh_from_db()
        self.assertEqual(self.adam_post.title, 'a new title')

    def test_user_cant_update_another_users_post(self):
        print("Testing user can't update another user's post")
        self.authenticate(self.adam)
        response = self.client.put(self.detail_url_brian, {'title': 'a new title', 'content': 'updated content'})
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
