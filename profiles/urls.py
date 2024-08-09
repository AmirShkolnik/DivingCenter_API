from django.urls import path
from .views import ProfileList, ProfileDetail, DeleteUserView

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('users/<int:pk>/', DeleteUserView.as_view(), name='user-delete'),
]
