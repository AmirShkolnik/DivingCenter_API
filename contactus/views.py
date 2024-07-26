from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import ContactSerializer
from .models import Contact
from django.shortcuts import get_object_or_404
from uuid import uuid4


class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Contact.objects.all()
            return Contact.objects.filter(email=self.request.user.email)
        return Contact.objects.none()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(deletion_token=uuid4())


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE' and self.request.user.is_staff:
            return [IsAdminUser()]
        return [AllowAny()]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        deletion_token = self.request.query_params.get('deletion_token')

    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        deletion_token = self.request.query_params.get('deletion_token')

        if user.is_authenticated:
            if user.is_staff or obj.email == user.email:
                return obj
        elif deletion_token and str(obj.deletion_token) == deletion_token:
            return obj
        return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"error": "You don't have permission to view this message"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"error": "You don't have permission to update this message"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=kwargs.pop('partial', False)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(
                {"error": "You don't have permission to delete this message"},
                status=status.HTTP_403_FORBIDDEN
            )

        self.perform_destroy(instance)
        return Response(
            {"message": "Contact deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
