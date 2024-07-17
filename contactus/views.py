from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import ContactSerializer
from .models import Contact
from uuid import uuid4

class ContactView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None):
        if pk:
            try:
                contact = Contact.objects.get(pk=pk)
                serializer = ContactSerializer(contact)
                return Response(serializer.data)
            except Contact.DoesNotExist:
                return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            return Response({
                "id": contact.id,
                "deletion_token": str(contact.deletion_token), 
                "message": "Your message has been sent successfully!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            # Keep the old deletion token
            updated_contact = serializer.save(deletion_token=contact.deletion_token)
            return Response({
                "id": updated_contact.id,
                "deletion_token": str(contact.deletion_token),
                "message": "Your message has been updated successfully!"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"error": "No contact ID provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            contact = Contact.objects.get(pk=pk)
            deletion_token = request.query_params.get('deletion_token')
            if contact.deletion_token and str(contact.deletion_token) == deletion_token:
                contact.delete()
                return Response({"message": "Contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Invalid deletion token"}, status=status.HTTP_403_FORBIDDEN)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
