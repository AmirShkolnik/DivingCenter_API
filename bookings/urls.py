from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from courses.views import CourseViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]