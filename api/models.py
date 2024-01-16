# models.py

from django.db import models

class Manufacturer(models.Model):
    company_name = models.CharField(max_length=30)
    country_manufacturer = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name
