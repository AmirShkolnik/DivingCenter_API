from rest_framework import serializers
from django.utils import timezone
from .models import Booking
from courses.models import Course


class SimpleCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_type', 'price']


class BookingSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.title')
    course_details = SimpleCourseSerializer(source='course', read_only=True)
    time = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])
    confirm_changes = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'date', 'time', 'course', 'course_name',
            'course_details', 'additional_info', 'created_at',
            'confirm_changes',
        ]
        read_only_fields = ['user']
        extra_kwargs = {'course': {'required': True}}

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError(
                "You can't book a date in the past."
            )
        if value.day != 10:
            raise serializers.ValidationError(
                "Bookings are only available on the 10th of each month."
            )
        return value

    def validate_time(self, value):
        if value.strftime('%H:%M') not in ['09:00', '15:00']:
            raise serializers.ValidationError(
                "Bookings are only available at 09:00 or 15:00."
            )
        return value

    def validate_course(self, value):
        if value is None:
            raise serializers.ValidationError("Please select a course.")
        return value

    def validate(self, data):
        course = data.get('course')
        date = data.get('date')
        time = data.get('time')
        user = self.context['request'].user

        if self.instance:
            existing_booking = Booking.objects.filter(
                user=user,
                course=course,
                date=date,
                time=time
            ).exclude(id=self.instance.id).exists()
        else:
            existing_booking = Booking.objects.filter(
                user=user,
                course=course,
                date=date,
                time=time
            ).exists()

        if existing_booking:
            raise serializers.ValidationError(
                "A booking for this course, date, and time already exists."
                "Please choose a different date or time."
            )

        if self.instance:
            critical_fields = ['date', 'time', 'course']
            critical_changes = any(
                data.get(field) != getattr(self.instance, field)
                for field in critical_fields
            )
            if critical_changes and not data.get('confirm_changes'):
                raise serializers.ValidationError({
                    "Friendly reminder": (
                        "Changing the time, date, or course type "
                        "might result in losing your spot."
                    )
                })

        return data
