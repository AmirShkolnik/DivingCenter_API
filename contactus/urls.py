from django.urls import path
from .views import ContactView

urlpatterns = [
    path('contactus/', ContactView.as_view(), name='contact'),
]