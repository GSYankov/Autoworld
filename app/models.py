from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case


class Image(models.Model):
    image = models.ImageField(upload_to='images')

