from django.urls import path

from .views import (RegisterView,
                    VerifyEmail,
                    LoginAPIView,
                    RequestPasswordResetEmail,
                    PasswordTokenCheckAPI,
                    SetNewPasswordAPIView,
                    LogoutAPIView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('verify-email/', VerifyEmail.as_view(), name="verify_email"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('password-reset-email/',
         RequestPasswordResetEmail.as_view(),
         name="password_reset_email"),
    path('password-token-check/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(),
         name="password_token_check"),
    path('set-new-password/',
         SetNewPasswordAPIView.as_view(),
         name="set_new_password"),
    path('logout/', LogoutAPIView.as_view(), name="logout")
]