from django.urls import path

from ecom.products.views import list_products, create_product, details_of_product, edit_product, delete_product, \
    review_product

urlpatterns = [
    path('', list_products, name='list products'),
    path('create/', create_product, name='create product'),
    path('product/<int:pk>/', details_of_product, name='details of product'),
    path('product/<int:pk>/edit/', edit_product, name='edit product'),
    path('product/<int:pk>/delete/', delete_product, name='delete product'),
    path('product/<int:pk>/review', review_product, name='review product'),
]