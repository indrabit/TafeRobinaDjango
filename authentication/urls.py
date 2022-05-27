from django.urls import path
from .views import LoginAPIView,RegisterView,RequestPasswordResetEmailView,SetNewPasswordAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('password-reset/', RequestPasswordResetEmailView.as_view(), name="password-reset"),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name="password-reset-complete"),
]

