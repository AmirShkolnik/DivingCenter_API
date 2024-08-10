import logging
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from comments.models import Comment
from likes.models import Like
from posts.models import Post

logger = logging.getLogger(__name__)

# Define IsOwnerOrReadOnly permission
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

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
    lookup_field = 'id'

    def get_queryset(self):
        return Profile.objects.annotate(
            posts_count=Count('owner__post', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True)
        ).order_by('-created_at')

    def perform_destroy(self, instance):
        logger.info(f"Deleting profile for user {instance.owner.username}")
        instance.delete()

class DeleteUserView(APIView):
    """
    View to delete a user and their associated profile.
    Deletes all related data such as comments, likes, and posts.
    Only the user themselves or a superuser can perform this action.
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        user_to_del = get_object_or_404(User, pk=pk)

        # Ensure the request is made by the user themselves or a superuser
        if request.user != user_to_del and not request.user.is_superuser:
            logger.warning(
                f"Unauthorized deletion attempt by {request.user.username} on {user_to_del.username}'s account from IP {request.META.get('REMOTE_ADDR')}"
            )
            return Response({"detail": "You are not allowed to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Delete related objects first
        Comment.objects.filter(owner=user_to_del).delete()
        Like.objects.filter(owner=user_to_del).delete()
        Post.objects.filter(owner=user_to_del).delete()

        # Delete the profile if it exists
        profile_to_del = getattr(user_to_del, 'profile', None)
        if profile_to_del:
            profile_to_del.delete()
            logger.info(f"Profile of user {user_to_del.username} deleted successfully.")

        # Delete the user
        user_to_del.delete()
        logger.info(f"User {user_to_del.username} deleted successfully.")

        # Log out the user if they are deleting their own account
        if request.user == user_to_del:
            logout(request)
            logger.info(f"User {user_to_del.username} logged out successfully.")

        return Response({"detail": "The user account and profile have been successfully deleted."}, status=status.HTTP_200_OK)