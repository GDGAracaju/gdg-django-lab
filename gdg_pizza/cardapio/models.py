from django.db import models

class Product (models.Model)
	name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False, blank=True)