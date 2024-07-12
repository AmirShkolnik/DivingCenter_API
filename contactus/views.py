from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import ContactSerializer
from .models import Contact

class ContactView(APIView):
    def get(self, request, pk=None):
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to view this content."}, status=status.HTTP_403_FORBIDDEN)
        
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
            serializer.save()
            return Response({
                "id": contact.id,
                "message": "Your message has been updated successfully!"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to delete this content."}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            contact = Contact.objects.get(pk=pk)
            contact.delete()
            return Response({"message": "Contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def delete_contact(request, pk):
#    try:
#        contact = Contact.objects.get(pk=pk)
#        contact.delete()
#        return Response({"message": "Contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#    except Contact.DoesNotExist:
#        return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)