from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from . import serializers, models


class ProductViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating Products."""

    queryset = models.Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get', 'post', 'head', 'put', 'patch']


class OrderViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating Orders."""

    queryset = models.Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.OrderSerializer
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)