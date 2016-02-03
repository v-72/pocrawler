from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
	product_name = models.CharField(max_length=30)
	price = models.CharField(max_length=7)