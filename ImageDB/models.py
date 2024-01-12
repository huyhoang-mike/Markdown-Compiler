from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField('Venue name', max_length=120)
    venue_image = models.ImageField(null=True, blank=True, upload_to='.')

    def __str__(self):
        return self.name