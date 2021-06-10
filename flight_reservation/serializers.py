from rest_framework import serializers, fields

from . import models


class ProductSerializer(serializers.ModelSerializer):
    """serializer for Product objects."""

    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ['created', 'updated']


class OrderSerializer(serializers.ModelSerializer):
    """serializer for Order objects."""

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ['created', 'updated']


