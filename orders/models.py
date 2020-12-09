from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.description

class Offer(models.Model):
    order = models.ForeignKey(
        Order, on_delete=CASCADE
    )

    trader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isAccepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.order.description
