from django.contrib import admin

from ecom.products.models import Product, Review


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating')


admin.site.register(Product, ProductsAdmin)
admin.site.register(Review, ReviewsAdmin)