from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import generics, filters, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    """
    List all profiles. Read-only access for all users.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['owner__following__followed__profile']
    ordering_fields = ['posts_count',
                       'followers_count', 'following_count',
                       'owner__following__created_at',
                       'owner__followed__created_at']

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a profile.
    Read access for all users, write access only for the owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

class DeleteUserView(APIView):
    """
    View to delete a user and their associated profile.
    Only the user themselves can delete their account.
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
            # Ensure that only the user themselves can delete their account
            if request.user == user:
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
