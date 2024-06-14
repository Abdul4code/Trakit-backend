from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout
from rest_framework import permissions, authentication
from django.contrib.auth.hashers import make_password

# import serializers
from users.serializers import RegisterSerializer, LoginSerializer

class Register(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        if data.get('password') != data.get('confirm_password'):
            return Response({'error': 'Password and Confirm password do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()

        return Response(serializer.data)

class Login(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh =  RefreshToken.for_user(user)
        accessToken = refresh.access_token
        login(request=request, user=user)

        return Response({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'Refresh Token': str(refresh),
            'Access Token': str(accessToken)
        })
    
class Logout(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': "User has been logged out"})

class UpdatePassword(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        user = User.objects.get(username=username)
        serializer = RegisterSerializer(instance=user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(data.get('password'))
        serializer.save()

        return Response(serializer.data)
