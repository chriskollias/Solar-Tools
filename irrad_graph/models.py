from django.db import models


# Create your models here.
class IrradGraphInputs(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    year = models.IntegerField()