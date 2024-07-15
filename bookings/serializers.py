from rest_framework import serializers
from django.utils import timezone
from .models import Booking
from courses.models import Course
from courses.serializers import CourseSerializer

class BookingSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.title')
    course_details = CourseSerializer(source='course', read_only=True)
    time = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])

    class Meta:
        model = Booking
        fields = ['id', 'user', 'date', 'time', 'course', 'course_name', 'course_details', 'additional_info', 'created_at']
        read_only_fields = ['user']

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Cannot book a date in the past.")
        if value.day != 10:
            raise serializers.ValidationError("Bookings are only available on the 10th of each month.")
        return value

    def validate_time(self, value):
        if value.strftime('%H:%M') not in ['09:00', '15:00']:
            raise serializers.ValidationError("Bookings are only available at 09:00 or 15:00.")
        return value

    def validate_course(self, value):
        if value is None:
            raise serializers.ValidationError("Course selection is required.")
        return value

    def validate(self, data):
        course = data['course']
        date = data['date']
        time = data['time']

        existing_booking = Booking.objects.filter(
            course=course,
            date=date,
            time=time
        ).exists()

        if existing_booking:
            raise serializers.ValidationError("A booking for this course, date, and time already exists.")

        return data