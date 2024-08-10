from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.profile = self.user.profile
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_profile_creation(self):
        self.assertEqual(self.profile.owner.username, 'testuser')
        self.assertEqual(self.profile.name, '')
        self.assertEqual(self.profile.content, '')
        self.assertIsNotNone(self.profile.created_at)
        self.assertIsNotNone(self.profile.updated_at)

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "testuser's profile")

    def test_profile_auto_create_on_user_creation(self):
        new_user = User.objects.create_user(username='newuser',
                                            password='newpassword')
        self.assertTrue(hasattr(new_user, 'profile'))

    def test_profile_update(self):
        self.profile.name = 'Updated Name'
        self.profile.content = 'Updated content.'
        self.profile.save()
        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.name, 'Updated Name')
        self.assertEqual(updated_profile.content, 'Updated content.')

    def test_profile_image_default(self):
        self.assertEqual(self.profile.image, '../default_profile_ameb12')

    def test_profile_ordering(self):
        older_user = User.objects.create_user(username='olderuser',
                                              password='password')
        older_profile = older_user.profile
        older_profile.created_at = timezone.now() - timedelta(days=1)
        older_profile.save()

        newer_user = User.objects.create_user(username='neweruser',
                                              password='password')
        newer_profile = newer_user.profile

        newer_profile.created_at = timezone.now()
        newer_profile.save()

        profiles = Profile.objects.all().order_by('-created_at')
        self.assertEqual(list(profiles), [newer_profile,
                         self.profile, older_profile])