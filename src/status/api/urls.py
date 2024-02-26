from django.urls import path, include

from .views import (
    StatusAPIView, 
    StatusAPIDetailView,
    )

urlpatterns = [
    path('', StatusAPIView.as_view(), name='list'),
    path('(?P<id>\d+)/', StatusAPIDetailView.as_view(), name='detail'),
]
