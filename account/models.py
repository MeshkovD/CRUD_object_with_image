from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username


class Events(models.Model):
    pass