from django.db import models

class SimpleAddPicture(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
