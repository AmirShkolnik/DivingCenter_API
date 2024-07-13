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
        try:
            date = datetime.strptime(request.data['date'], '%Y-%m-%d').date()
            if date.day != 10:
                return Response({"date": ["Bookings are only available on the 10th of each month."]}, status=status.HTTP_400_BAD_REQUEST)

            booking_time = datetime.strptime(request.data['time'], '%H:%M').time()
            if booking_time not in [time(9, 0), time(15, 0)]:
                return Response({"time": ["Bookings are only available at 09:00 or 15:00."]}, status=status.HTTP_400_BAD_REQUEST)

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

class DivingCourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DivingCourse.objects.all()
    serializer_class = DivingCourseSerializer