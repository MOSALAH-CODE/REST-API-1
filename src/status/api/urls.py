from django.urls import path, include

from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    )

app_name = 'status'  # Define the app_name attribute


urlpatterns = [
    path('', StatusAPIView.as_view(), name='list'),
    path('<id>/', StatusAPIDetailView.as_view(), name='detail'),
]
