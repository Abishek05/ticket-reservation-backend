from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.settings import api_settings

from . import serializers, models
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


class UserViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating Products."""

    queryset = models.User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserSerilaizer
    http_method_names = ['get', 'post', 'head', 'put', 'patch']


# class LoginViewSet(viewsets.ModelViewSet):
#
#     queryset = models.User.objects.all()
#     serializer_class = AuthTokenSerializer
#
#     def create(self, request):
#
#         return ObtainAuthToken().post(request)

class LoginViewSet(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


