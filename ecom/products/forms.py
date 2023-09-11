from django import forms

from ecom.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(ProductForm):
    pass