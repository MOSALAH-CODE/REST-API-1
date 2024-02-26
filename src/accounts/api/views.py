from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework_jwt.settings import api_settings

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import AnonPermissionOnly
from .serializers import UserRegisterSerializer, MyTokenObtainPairSerializer

User = get_user_model()


class AuthAPIView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)

        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({"detail": "Invalid credentials"}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset                = User.objects.all()
    serializer_class        = UserRegisterSerializer
    permission_classes      = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# class RegisterAPIView(APIView):
#     permission_classes      = [permissions.AllowAny]
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return Response({'detail': 'You are already registered and are authenticated.'}, status=400)
#         data = request.data
#         username        = data.get('username') # username or email address
#         email           = data.get('username')
#         password        = data.get('password')
#         password2       = data.get('password2')
#         qs = User.objects.filter(
#                 Q(username__iexact=username)|
#                 Q(email__iexact=username)
#             )
#         if password != password2:
#             return Response({"password": "Password must match."}, status=401)
#         if qs.exists():
#             return Response({"detail": "This user already exists"}, status=401)
#         else:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             # payload = jwt_payload_handler(user)
#             # token = jwt_encode_handler(payload)
#             # response = jwt_response_payload_handler(token, user, request=request)
#             # return Response(response, status=201)
#             return Response({'detail': "Thank you for registering. Please verify your email."}, status=201)
#         return Response({"detail": "Invalid Request"}, status=400)




