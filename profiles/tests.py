from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.utils import timezone
from datetime import timedelta

class ProfileModelTests(TestCase):

    def setUp(self):
        """Create a user for testing."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = self.user.profile

    def test_profile_creation(self):
        """Test that a profile is created correctly."""
        self.assertEqual(self.profile.owner.username, 'testuser')
        self.assertEqual(self.profile.name, '')
        self.assertEqual(self.profile.content, '')
        self.assertIsNotNone(self.profile.created_at)
        self.assertIsNotNone(self.profile.updated_at)

    def test_profile_str(self):
        """Test the string representation of the profile."""
        self.assertEqual(str(self.profile), "testuser's profile")

    def test_profile_auto_create_on_user_creation(self):
        """Test that a profile is automatically created when a user is created."""
        new_user = User.objects.create_user(username='newuser', password='newpassword')
        self.assertTrue(hasattr(new_user, 'profile'))

    def test_profile_update(self):
        """Test that the profile can be updated."""
        self.profile.name = 'Updated Name'
        self.profile.content = 'Updated content.'
        self.profile.save()
        
        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.name, 'Updated Name')
        self.assertEqual(updated_profile.content, 'Updated content.')

    def test_profile_image_default(self):
        """Test that the profile uses the default image if none is provided."""
        self.assertEqual(self.profile.image, '../default_profile_ameb12')

    def test_profile_ordering(self):
        """Test that profiles are ordered by created_at descending."""
        # Create an older user/profile
        older_user = User.objects.create_user(username='olderuser', password='password')
        older_profile = older_user.profile
        older_profile.created_at = timezone.now() - timedelta(days=1)
        older_profile.save()
        
        # Create a newer user/profile
        newer_user = User.objects.create_user(username='neweruser', password='password')
        newer_profile = newer_user.profile
        
        # Ensure the newest profile has the latest timestamp
        newer_profile.created_at = timezone.now()
        newer_profile.save()

        # Retrieve profiles ordered by created_at descending
        profiles = Profile.objects.all().order_by('-created_at')

        # Assert the order
        self.assertEqual(list(profiles), [newer_profile, self.profile, older_profile])
