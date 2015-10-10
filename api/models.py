from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    ean_code = models.CharField(max_length=256)
    carritus_id = models.CharField(max_length=256)