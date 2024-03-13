from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers.user_serializers import UserLoginSerializer, UserSerializer, UserDetailSerializer
from rest_framework import permissions


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserSignupView(
    generics.CreateAPIView,
    mixins.CreateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

    # def create(self, request, *args, **kwargs):
    #     request.data['password'] = make_password(request.data['password'])
    #     return super().create(request, *args, **kwargs)


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = get_tokens_for_user(user)
            return Response({'message': 'Login successful', 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user
