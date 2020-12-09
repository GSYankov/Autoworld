from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='images',
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
