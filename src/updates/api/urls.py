from django.urls import path

from .views import (
            UpdateModelDetailAPIView,
            UpdateModelListAPIView 
    )

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()), # api/updates/ - List/Create
    path('(?P<id>\d+)/', UpdateModelDetailAPIView.as_view()),
]