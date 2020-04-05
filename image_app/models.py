from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import signals



class SimpleAddPicture(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


def create_user(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username

signals.post_save.connect(create_user, sender=User)