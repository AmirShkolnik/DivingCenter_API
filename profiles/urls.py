from django.urls import path
from .views import DeleteUserView, ProfileList, ProfileDetail

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),  # Use 'id' here
    path('users/<int:pk>/', DeleteUserView.as_view(), name='user-delete'),
]