from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Booking, DivingCourse
from .serializers import BookingSerializer, DivingCourseSerializer
from datetime import datetime, time
import logging

logger = logging.getLogger(__name__)

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Add this line to define the queryset

    def get_queryset(self):
        user_bookings = Booking.objects.filter(user=self.request.user)
        logger.info(f"Fetched {user_bookings.count()} bookings for user {self.request.user.username}")
        return user_bookings

    def create(self, request, *args, **kwargs):
        logger.info(f"Attempting to create booking for user {request.user.username}")
        try:
            date = datetime.strptime(request.data['date'], '%Y-%m-%d').date()
            if date.day != 10:
                return Response({"error": "Bookings are only available on the 10th of each month."}, status=status.HTTP_400_BAD_REQUEST)

            booking_time = datetime.strptime(request.data['time'], '%H:%M').time()
            if booking_time not in [time(9, 0), time(15, 0)]:
                return Response({"error": "Bookings are only available at 09:00 or 15:00."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            logger.info(f"Booking created successfully for user {request.user.username}")
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except KeyError as e:
            logger.error(f"Missing required field: {str(e)}")
            return Response({"error": f"Missing required field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            logger.error(f"Invalid date or time format: {str(e)}")
            return Response({"error": f"Invalid date or time format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error creating booking: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class DivingCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DivingCourse.objects.all()
    serializer_class = DivingCourseSerializer