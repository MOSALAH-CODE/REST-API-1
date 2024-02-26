from django.urls import path, include
from django.contrib import admin


from .views import UserDetailAPIView, UserStatusAPIView

app_name = 'accounts.user'  # Define the app_name attribute

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<username>/status/', UserStatusAPIView.as_view(), name='status-list'),
]