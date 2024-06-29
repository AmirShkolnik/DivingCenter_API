from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [

    path('', include(router.urls)),
]