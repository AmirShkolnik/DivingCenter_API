from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, DivingCourse
from .serializers import BookingSerializer, DivingCourseSerializer
from datetime import datetime, time
import logging

logger = logging.getLogger(__name__)

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the booking.
        return obj.user == request.user

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the bookings
        for the currently authenticated user.
        """
        user = self.request.user
        return Booking.objects.filter(user=user)

def create(self, request, *args, **kwargs):
    logger.info(f"Attempting to create booking for user {request.user.username}")
    errors = {}

    try:
        date_str = request.data.get('date', '')
        time_str = request.data.get('time', '')
        course_id = request.data.get('course')

        if not date_str:
            errors['date'] = ["Date is required."]
        else:
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                if date.day != 10:
                    errors['date'] = ["Bookings are only available on the 10th of each month."]
            except ValueError:
                errors['date'] = ["Invalid date format. Use YYYY-MM-DD."]

        if not time_str:
            errors['time'] = ["Time is required."]
        else:
            try:
                booking_time = datetime.strptime(time_str, '%H:%M').time()
                if booking_time not in [time(9, 0), time(15, 0)]:
                    errors['time'] = ["Bookings are only available at 09:00 or 15:00."]
            except ValueError:
                errors['time'] = ["Invalid time format. Use HH:MM."]

        if not course_id:
            errors['course'] = ["Course selection is required."]

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f"Booking created successfully for user {request.user.username}")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    except Exception as e:
        logger.error(f"Unexpected error creating booking: {str(e)}")
        return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DivingCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DivingCourse.objects.all()
    serializer_class = DivingCourseSerializer