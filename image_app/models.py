from django.db import models

class SimpleAddPicture(models.Model):
    title = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='images/', blank=False, null=False)

    def __str__(self):
        return self.title