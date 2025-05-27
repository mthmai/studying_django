from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Names(models.Model):
    name = models.CharField(max_length=60)
    yo = models.IntegerField(null=False)


class Products(models.Model):
    product_name = models.CharField(max_length=80)
    preco = models.FloatField(null=False)