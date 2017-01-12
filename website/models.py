from __future__ import unicode_literals
from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.product_name

	def cheapo(self):
		return self.price < 10

class CartItem(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()

class Cart(models.Model):
	items = models.ManyToManyField(CartItem)
	user = models.ForeignKey(AUTH_USER_MODEL)
