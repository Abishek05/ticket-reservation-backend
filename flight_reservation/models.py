from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


User = get_user_model()


ORDER_STATUS = (
    ('PENDING', 'Pending'),
    ('BOOKED', 'Booked'),
    ('REFUNDED', 'Refunded'),
    ('CANCELLED', 'Cancelled')
)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, validators=[MinValueValidator(Decimal('1.00'))])
    stock = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(choices=ORDER_STATUS, blank=True, null=True, max_length=25, default="PENDING")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order_status)




