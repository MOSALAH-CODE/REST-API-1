from django.urls import path, include
from django.contrib import admin


# from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token # accounts app
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AuthAPIView, RegisterAPIView
urlpatterns = [
    path('', AuthAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    # path('jwt/', obtain_jwt_token),
    path('jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('jwt/refresh/', refresh_jwt_token),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]