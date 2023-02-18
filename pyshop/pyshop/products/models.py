from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=3012)

class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=123123)
    discount = models.FloatField()
