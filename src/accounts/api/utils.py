from datetime import timedelta
from django.utils import timezone

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': str(token.access_token),
        'user': user.username,
        'expires': timezone.now() + timedelta(seconds=api_settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'])
    }