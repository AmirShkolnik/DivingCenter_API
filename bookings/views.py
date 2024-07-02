# views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, DivingCourse
from .serializers import BookingSerializer, DivingCourseSerializer
from datetime import datetime, time
import logging

logger = logging.getLogger(__name__)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_bookings = Booking.objects.filter(user=self.request.user)
        logger.info(f"Fetched {user_bookings.count()} bookings for user {self.request.user.username}")
        return user_bookings

    def create(self, request, *args, **kwargs):
        logger.info(f"Attempting to create booking for user {request.user.username}")
        # Check if the date is valid (10th of the month)
        date = datetime.strptime(request.data['date'], '%Y-%m-%d').date()
        if date.day != 10:
            return Response({"error": "Bookings are only available on the 10th of each month."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the time is valid (09:00 or 15:00)
        booking_time = datetime.strptime(request.data['time'], '%H:%M').time()
        if booking_time not in [time(9, 0), time(15, 0)]:
            return Response({"error": "Bookings are only available at 09:00 or 15:00."}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        logger.info(f"Booking created successfully for user {request.user.username}")
        return response


class DivingCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DivingCourse.objects.all()
    serializer_class = DivingCourseSerializer