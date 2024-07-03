from django.urls import path
from .views import ContactView, delete_contact

urlpatterns = [
    path('contactus/', ContactView.as_view(), name='contact'),
    path('contactus/<int:pk>/', ContactView.as_view(), name='contact-detail'),
    path('contactus/<int:pk>/delete/', delete_contact, name='delete-contact'),
]