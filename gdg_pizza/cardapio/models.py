# coding=UTF-8
import datetime
from django.db import models
from django.utils import timezone

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
	category = models.ForeignKey(Category, verbose_name='Categoria')
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
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Publicado recentemente?'

	def __unicode__(self):
		return self.name
