from django.contrib import admin
from cardapio.models import Product, Category

class ProductsInline(admin.StackedInline):
    model = Product
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'price', 'featured', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['name', 'description']
	fieldsets = [
		(None, 		 {'fields': ['category', 'name', 'featured']}),
		('Detalhes', {'fields': ['price', 'description']})
	]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)