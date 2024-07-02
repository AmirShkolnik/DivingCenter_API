from rest_framework import serializers
from .models import Booking, DivingCourse

class DivingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivingCourse
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.get_name_display')

    class Meta:
        model = Booking
        fields = ['id', 'user', 'date', 'time', 'course', 'course_name', 'additional_info', 'created_at']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate_course(self, value):
        if not DivingCourse.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid course selection.")
        return value

    def validate_date(self, value):
        if value.day != 10:
            raise serializers.ValidationError("Bookings are only available on the 10th of each month.")
        return value

    def validate_time(self, value):
        if value.strftime('%H:%M') not in ['09:00', '15:00']:
            raise serializers.ValidationError("Bookings are only available at 09:00 or 15:00.")
        return value