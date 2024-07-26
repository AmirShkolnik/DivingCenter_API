from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Contact
import uuid


class ContactAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass',
            email='testuser@example.com'
        )
        self.admin_user = User.objects.create_superuser(
            username='admin', password='adminpass',
            email='admin@example.com'
        )
        self.contact1 = Contact.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Subject 1",
            message="Message 1",
            deletion_token=uuid.uuid4()
        )
        self.contact2 = Contact.objects.create(
            name="John Doe",
            email="testuser@example.com",
            subject="Subject 2",
            message="Message 2",
            deletion_token=uuid.uuid4()
        )
        self.list_create_url = reverse('contact-list-create')
        self.detail_url = reverse('contact-detail',
                                  kwargs={'pk': self.contact1.pk})

    def test_create_contact(self):
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'subject': 'New Subject',
            'message': 'New Message'
        }
        response = self.client.post(self.list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 3)

    def test_list_contacts_unauthenticated(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_contacts_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # User is seeing all contacts

    def test_list_contacts_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Admin is seeing all contacts

    def test_retrieve_contact_unauthenticated(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_contact_authenticated_owner(self):
        self.client.force_authenticate(user=self.user)
        detail_url = reverse('contact-detail', kwargs={'pk': self.contact2.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_contact_authenticated_non_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_contact_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_contact_unauthenticated(self):
        data = {'subject': 'Updated Subject'}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_contact_authenticated_owner(self):
        self.client.force_authenticate(user=self.user)
        detail_url = reverse('contact-detail', kwargs={'pk': self.contact2.pk})
        data = {'subject': 'Updated Subject'}
        response = self.client.patch(detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Contact.objects.get(pk=self.contact2.pk).subject,
            'Updated Subject'
        )

    def test_delete_contact_unauthenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_contact_authenticated_non_admin(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_contact_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 1)

    def test_delete_contact_with_token(self):
        url = (f"{self.detail_url}?"
               f"deletion_token={self.contact1.deletion_token}")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.count(), 1)
