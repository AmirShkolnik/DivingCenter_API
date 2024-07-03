from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, DivingCourseViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'diving-courses', DivingCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]