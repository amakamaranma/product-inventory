from django.db import models
from django.db.models import CharField


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=300)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    expiry_date = models.DateField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # brand = models.CharField(max_length=10)
    supply_date = models.DateField(max_length=2000, null=True, blank=True)

    def __str__(self) -> CharField:
        return self.name







