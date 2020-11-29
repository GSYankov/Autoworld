from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case


class Image(models.Model):
    image = models.ImageField(upload_to='images')


class Offer(models.Model):
    trader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
