from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .serializers import SignUpSerializer
from .models import CustomUser
from .tokens import create_jwt_pair_for_user

class SignUpView(generics.GenericAPIView):

    serializer_class = SignUpSerializer
    permission_classes = []
    @swagger_auto_schema(
        operation_summary="Register New User",
        operation_description="This register a new user with given proper data",
    )
    def post(self, request: Request):
        request_data = request.data

        serializer = self.serializer_class(data=request_data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "user Created successfuly",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = []
    @swagger_auto_schema(
        operation_summary="Login In User",
        operation_description="This log user into a project",
    )
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            
            response = {
                "message": "You logged in successfully",
                "tokens" : tokens,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {"message" : "Invalid user email or password "}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_summary="Get User Authentication",
        operation_description="This returns user authnetication information",
    )       
    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)