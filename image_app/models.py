from django.db import models

class SimpleAddPicture(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.old_title = self.title
    #
    # def save(self, *args, **kwargs):
    #     if self.old_title and not self.title:
    #         self.paid_time = timezone.now()
    #     return super().save(*args, **kwargs)