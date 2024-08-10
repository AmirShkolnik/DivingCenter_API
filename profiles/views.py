import logging
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from likes.models import Like
from comments.models import Comment
from bookings.models import Booking
from courses.models import Review

logger = logging.getLogger(__name__)

class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True)
        ).order_by('-created_at')

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True)
        ).order_by('-created_at')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.owner:
            logger.info(f"Deleting profile for user {instance.owner.username}")

            # Delete related objects
            self.delete_related_objects(instance.owner)

            self.perform_destroy(instance)
            
            # Deactivate the user
            user = request.user
            user.is_active = False
            user.save()
            logger.info(f"User {user.username} deactivated successfully.")
            
            # Log out the user
            logout(request)
            logger.info(f"User {user.username} logged out successfully.")
            
            # Redirect to the root URL
            return HttpResponseRedirect('/')
        else:
            logger.warning(f"User {request.user.username} attempted to delete profile of {instance.owner.username} without permission.")
            return Response({"detail": "You do not have permission to delete this profile."}, status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        instance.delete()

    def delete_related_objects(self, user):
        Comment.objects.filter(owner=user).delete()
        Like.objects.filter(owner=user).delete()
        Review.objects.filter(user=user).delete()
        Booking.objects.filter(user=user).delete()
        logger.info(f"Deleted all related objects for user {user.username}")

class DeleteUserView(APIView):
    """
    View to delete a user and their associated profile.
    Only an admin can delete a user.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk, format=None):
        # Retrieve the user to be deleted
        user_to_del = get_object_or_404(User, pk=pk)
        profile_to_del = getattr(user_to_del, 'profile', None)

        # Check if the request is made by an admin
        if not request.user.is_staff:
            logger.warning(f"User {request.user.username} attempted to delete user {user_to_del.username} without admin permission.")
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Handle the deletion of the profile and user
        if profile_to_del:
            profile_to_del.delete()
            logger.info(f"Profile of user {user_to_del.username} deleted successfully.")

        user_to_del.delete()
        logger.info(f"User {user_to_del.username} deleted successfully.")

        return Response({"detail": "The user account has been successfully deleted."}, status=status.HTTP_200_OK)