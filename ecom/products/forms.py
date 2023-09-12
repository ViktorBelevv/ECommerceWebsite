from django import forms

from ecom.core.boostrap_mixins import BoostrapFormMixin
from ecom.products.models import Product


class ProductForm(BoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(ProductForm):
    pass


class EditProductForm(ProductForm):
    pass