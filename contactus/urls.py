from django.urls import path
from .views import ContactListCreateView, ContactDetailView

urlpatterns = [
    path('contactus/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contactus/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]