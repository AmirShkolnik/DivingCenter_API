from rest_framework import serializers
from django.utils import timezone
from .models import Booking, DivingCourse

class DivingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivingCourse
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.get_course_type_display')
    time = serializers.TimeField(format='%H:%M', input_formats=['%H:%M'])

    class Meta:
        model = Booking
        fields = ['id', 'user', 'date', 'time', 'course', 'course_name', 'additional_info', 'created_at']
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

    def validate(self, data):
        if data['course'] is None:
            raise serializers.ValidationError({"course": "Course selection is required."})
        return data