from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, time, timedelta
from .models import Booking
from courses.models import Course
from .serializers import BookingSerializer

def next_valid_date():
    today = date.today()
    if today.day <= 10:
        return date(today.year, today.month, 10)
    next_month = today.replace(day=1) + timedelta(days=32)
    return date(next_month.year, next_month.month, 10)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', course_type='Online', price=100.00)
        self.booking = Booking.objects.create(
            user=self.user,
            date=next_valid_date(),
            time=time(9, 0),
            course=self.course,
            additional_info='Test info',
        )

    def test_booking_creation(self):
        self.assertEqual(str(self.booking), f'testuser - Test Course on {self.booking.date} at 09:00:00')

    def test_booking_date_not_10th(self):
        invalid_date = next_valid_date().replace(day=11)
        data = {
            'user': self.user.id,
            'date': invalid_date,
            'time': '09:00',
            'course': self.course.id,
            'additional_info': 'Test info',
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)

class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.course = Course.objects.create(title='Test Course', course_type='Online', price=100.00)
        self.booking_data = {
            'date': next_valid_date().strftime('%Y-%m-%d'),
            'time': '09:00',
            'course': self.course.id,
            'additional_info': 'Test info',
        }
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('booking-list')

    def test_create_booking(self):
        response = self.client.post(self.list_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().user, self.user)

    def test_create_booking_invalid_date(self):
        invalid_date = next_valid_date().replace(day=11)
        self.booking_data['date'] = invalid_date.strftime('%Y-%m-%d')
        response = self.client.post(self.list_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('date', response.data)

    def test_create_booking_invalid_time(self):
        self.booking_data['time'] = '10:00'
        response = self.client.post(self.list_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('time', response.data)

    def test_create_duplicate_booking(self):
        self.client.post(self.list_url, self.booking_data, format='json')
        response = self.client.post(self.list_url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_booking(self):
        booking = Booking.objects.create(
            user=self.user, 
            date=next_valid_date(), 
            time=time(9, 0), 
            course=self.course
        )
        url = reverse('booking-detail', kwargs={'pk': booking.id})
        self.booking_data['time'] = '15:00'
        response = self.client.put(url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Booking.objects.get().time, time(15, 0))

    def test_delete_booking(self):
        booking = Booking.objects.create(
            user=self.user, 
            date=next_valid_date(), 
            time=time(9, 0), 
            course=self.course
        )
        url = reverse('booking-detail', kwargs={'pk': booking.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

    def test_get_bookings(self):
        Booking.objects.create(
            user=self.user, 
            date=next_valid_date(), 
            time=time(9, 0), 
            course=self.course
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_booking_detail(self):
        booking = Booking.objects.create(
            user=self.user, 
            date=next_valid_date(), 
            time=time(9, 0), 
            course=self.course
        )
        url = reverse('booking-detail', kwargs={'pk': booking.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], booking.id)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_booking_no_course(self):
        data = self.booking_data.copy()
        data.pop('course')
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('course', response.data)