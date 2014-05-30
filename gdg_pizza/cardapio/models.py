# coding=UTF-8
import datetime
from django.db import models

class Category(models.Model):
	name = models.CharField(verbose_name='Nome', max_length=100,
							help_text='O nome da categoria')
	created_on = models.DateTimeField(auto_now_add=True, 
							verbose_name='Criado em')
	updated_on = models.DateTimeField(auto_now=True, 
							verbose_name='Atualizado em')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['name']


class Product (models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField('nome', max_length=100)
	price = models.DecimalField('preço', max_digits=6, decimal_places=2)
	description = models.TextField('descrição', blank=True)
	featured = models.BooleanField('destaque', default=False, blank=True)
	pub_date = models.DateTimeField('data de publicação', auto_now_add=True)

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['name']


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __unicode__(self):
		return self.name
