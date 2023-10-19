from rest_framework_simplejwt.views import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
import jwt
from django.contrib.auth.models import update_last_login
from .. import settings
from rest_framework import status
from rest_framework.response import Response
from . import models
from .serializers import UserSerializer, StudentRegistrationSerializer, StudentProfileSerializerAlt
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import generics


# Create your views here.


class LoginUser(TokenViewBase):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        status_code = status.HTTP_200_OK
        data = serializer.validated_data
        payload = jwt.decode(jwt=data['access'], key=settings.SECRET_KEY, algorithms=['HS256'])['user_id']
        user = models.User.objects.get(id=payload)
        update_last_login(None, user)
        us = UserSerializer(user, fields=self.get_fields(user))
        response = {
            'success': True,
            'message': 'User logged in  successfully',
            "token": data['access'],
            "refresh": data['refresh'],
            "user": us.data,

        }
        return Response(response, status=status_code)

    def get_fields(self, user):
        if user.is_staff or user.is_superuser:
            return "is_staff", 'is_student', 'student_profile'
        else:
            return "is_staff", "is_superuser"


class RefreshUser(TokenViewBase):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        status_code = status.HTTP_200_OK
        data = serializer.validated_data
        payload = jwt.decode(jwt=data['access'], key=settings.SECRET_KEY, algorithms=['HS256'])['user_id']
        user = models.User.objects.get(id=payload)
        update_last_login(None, user)
        response = {
            "token": data['access'],
            "refresh": data['refresh'],
        }

        return Response(response, status=status_code)


class StudentRegistrationView(CreateAPIView):
    serializer_class = StudentRegistrationSerializer

    # permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': True,
            'status code': status_code,
            'message': 'User registered  successfully',
        }
        return Response(response, status=status_code)


class StudentListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return models.User.objects.filter(is_student=True)
