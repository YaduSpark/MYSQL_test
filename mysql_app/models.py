from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ProductManufacturer(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    category = models.ForeignKey(ProductCategory, related_name='category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(ProductManufacturer, related_name='manufacturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title