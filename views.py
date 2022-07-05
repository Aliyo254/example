from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, status, permissions, viewsets

from .permissions import *
from .serializers import *


class RegElderView(generics.GenericAPIView):
    serializer_class = ElderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Account created successfully."
        })


class RegResidentView(generics.GenericAPIView):
    serializer_class = ResidentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Account created successfully."
        })


class RegControllerView(generics.GenericAPIView):
    serializer_class = ControllerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Account created successfully."
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'is_elder': user.is_elder})


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class ResidentOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsResident]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ElderOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsElder]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ControllerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsController]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class Hood(generics.ListCreateAPIView):
    model = Hood
    serializer_class = HoodSerializer
    queryset = Hood.objects.all()


class HoodDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Hood
    serializer_class = HoodSerializer

    def get_queryset(self):
        pk = ''
        hood_details = Hood.objects.filter(id=pk)

        return hood_details