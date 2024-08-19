from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_bestseller = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)


