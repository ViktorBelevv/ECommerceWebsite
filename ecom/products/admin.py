from django.contrib import admin

from ecom.products.models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Product, ProductsAdmin)