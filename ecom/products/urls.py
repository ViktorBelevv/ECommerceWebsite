from django.urls import path

from ecom.products.views import list_products, create_product, details_of_product

urlpatterns = [
    path('', list_products, name='list products'),
    path('create/', create_product, name='create product'),
    path('product/<int:pk>', details_of_product, name='details of product')
]