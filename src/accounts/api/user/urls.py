from django.urls import path, include
from django.contrib import admin


from .views import UserDetailAPIView, UserStatusAPIView
urlpatterns = [
    path('(?P<username>\w+)/', UserDetailAPIView.as_view(), name='detail'),
    path('(?P<username>\w+)/status/', UserStatusAPIView.as_view(), name='status-list'),
]