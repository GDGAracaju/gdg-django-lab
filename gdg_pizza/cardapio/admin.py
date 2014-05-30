from django.contrib import admin
from cardapio.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		 {'fields': ['category', 'name', 'featured']}),
		('Detalhes', {'fields': ['price', 'description']})
	]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)