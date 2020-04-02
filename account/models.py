from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import signals


def create_user(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)


class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username

    # class Meta:
    #     verbose_name_plural = 'Профилей'
    #     verbose_name = 'Профиль'


signals.post_save.connect(create_user, sender=User)