from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch, MagicMock

def mocked_cloudinary_upload(*args, **kwargs):
    return {
        'public_id': 'test_public_id',
        'version': '1234567890',
        'signature': 'test_signature',
        'width': 100,
        'height': 100,
        'format': 'jpg',
        'resource_type': 'image',
        'created_at': '2021-01-01T00:00:00Z',
        'tags': [],
        'bytes': 1234,
        'type': 'upload',
        'etag': 'test_etag',
        'url': 'http://test.com/image.jpg',
        'secure_url': 'https://test.com/image.jpg',
        'original_filename': 'test_image'
    }

class CourseModelTest(TestCase):
    @patch('cloudinary.uploader.upload', side_effect=mocked_cloudinary_upload)
    def setUp(self, mock_upload):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(
            title='Test Course',
            slug='test-course',
            excerpt='This is a test course.',
            description='<p>This is a test description.</p>',
            course_type='OW',
            price=2000,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, 'Test Course')
        self.assertEqual(self.course.slug, 'test-course')
        self.assertEqual(self.course.price, 2000)

    def test_course_str_method(self):
        self.assertEqual(str(self.course), 'Test Course')

class CourseSerializerTest(TestCase):
    @patch('cloudinary.uploader.upload', side_effect=mocked_cloudinary_upload)
    def setUp(self, mock_upload):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.course = Course.objects.create(
            title='Test Course',
            slug='test-course',
            excerpt='This is a test course.',
            description='<p>This is a test description.</p>',
            course_type='OW',
            price=2000,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )
        self.serializer = CourseSerializer(instance=self.course)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'slug', 'excerpt', 'description', 'course_type', 'image', 'price', 'price_display', 'reviews', 'average_rating', 'created_at', 'updated_at'])

class CourseViewsTest(TestCase):
    @patch('cloudinary.uploader.upload', side_effect=mocked_cloudinary_upload)
    def setUp(self, mock_upload):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345', is_staff=True)
        self.course = Course.objects.create(
            title='Test Course',
            slug='test-course',
            excerpt='This is a test course.',
            description='<p>This is a test description.</p>',
            course_type='OW',
            price=2000,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )
        self.client.force_authenticate(user=self.user)

    def test_course_list_view(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('cloudinary.uploader.upload', side_effect=mocked_cloudinary_upload)
    def test_course_create_view(self, mock_upload):
        data = {
            'title': 'New Course',
            'slug': 'new-course',
            'excerpt': 'This is a new course.',
            'description': '<p>This is a new course description.</p>',
            'course_type': 'AOW',
            'price': 5000,
            'image': SimpleUploadedFile("new_image.jpg", b"file_content", content_type="image/jpeg")
        }
        response = self.client.post('/courses/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_detail_view(self):
        response = self.client.get(f'/courses/{self.course.slug}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_update_view(self):
        data = {'title': 'Updated Course'}
        response = self.client.patch(f'/courses/{self.course.slug}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, 'Updated Course')

    def test_course_delete_view(self):
        response = self.client.delete(f'/courses/{self.course.slug}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(slug=self.course.slug).exists())

    def test_unauthorized_course_create(self):
        self.client.logout()
        data = {
            'title': 'Unauthorized Course',
            'slug': 'unauthorized-course',
            'excerpt': 'This is an unauthorized course.',
            'description': '<p>This is an unauthorized course description.</p>',
            'course_type': 'RD',
            'price': 8000,
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        }
        response = self.client.post('/courses/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_course_update(self):
        self.client.logout()
        data = {'title': 'Unauthorized Update'}
        response = self.client.patch(f'/courses/{self.course.slug}/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_course_delete(self):
        self.client.logout()
        response = self.client.delete(f'/courses/{self.course.slug}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)