# coding=UTF-8
import datetime
from django.db import models

class Product (models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField(blank=True)
	featured = models.BooleanField(default=False, blank=True)
	pub_date = models.DateTimeField('data de publicação', auto_now_add=True)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.name