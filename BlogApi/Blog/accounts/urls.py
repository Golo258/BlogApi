from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="sign_up"),
    path("login/", views.LoginView.as_view(), name="log_in"),
    path("jwt/create", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzM0ODU2NywiaWF0IjoxNzE3MjYyMTY3LCJqdGkiOiI3MjZhM2VkZmJjMzY0Y2NjYmE4ZjNhYjEzYTk1OWY4MyIsInVzZXJfaWQiOjZ9.2YH_7Pu6RLJNODrXyQAyyxNPaUWK7IJEeh83kY7TZVs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MjYyNDY3LCJpYXQiOjE3MTcyNjIxNjcsImp0aSI6ImJhNTJjMzQ1ODk4YjQxMGZhM2E4YWNhZmMxZGM2NTZmIiwidXNlcl9pZCI6Nn0.eLVoTPbjmkIMdtZs1TndsRZdEaUUErwpBxXQBC3ehXs"
}