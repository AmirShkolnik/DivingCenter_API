from django.urls import path
from .views import ProfileList, ProfileDetail, ProfileDeleteAPIView

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/delete/', ProfileDeleteAPIView.as_view(), name='profile-delete'),
]
