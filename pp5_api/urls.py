"""
pp5_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from .views import root_route, logout_route


def health_check(request):
    # Simple endpoint for Render health checks (must return 200)
    return JsonResponse({"status": "ok"})


urlpatterns = [
    # Health check (set Render Health Check Path to /health/)
    path("health/", health_check, name="health_check"),

    # Root route (your existing view)
    path("", root_route),

    # Admin + auth
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/logout/", logout_route),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),

    # Editor
    path("tinymce/", include("tinymce.urls")),

    # App routes
    path("", include("profiles.urls")),
    path("", include("posts.urls")),
    path("", include("comments.urls")),
    path("", include("likes.urls")),
    path("", include("followers.urls")),
    path("", include("bookings.urls")),
    path("", include("contactus.urls")),
    path("", include("courses.urls")),
]
