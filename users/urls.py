from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .apps import UsersConfig
from .views import UserRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path(
        "register/", UserRegistrationView.as_view(), name="user-register"
    ),  # Регистрация пользователя
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Авторизация пользователя
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
