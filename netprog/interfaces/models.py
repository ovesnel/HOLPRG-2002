from django.db import models

# Create your models here.
class Interface(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    shutdown = models.BooleanField(default=False)
