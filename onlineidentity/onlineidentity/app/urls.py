from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import LoginUser, StudentRegistrationView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'login/?$', LoginUser.as_view()),
    re_path(r'login/refresh/?$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', StudentRegistrationView.as_view()),
]
