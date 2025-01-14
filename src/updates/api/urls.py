from django.urls import path

from .views import (
            UpdateModelDetailAPIView,
            UpdateModelListAPIView 
    )

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()), # api/updates/ - List/Create
    path('<id>/', UpdateModelDetailAPIView.as_view()),
]