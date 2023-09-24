from django import forms

from ecom.core.boostrap_mixins import BoostrapFormMixin
from ecom.products.models import Product, Review


class ProductForm(BoostrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(ProductForm):
    pass


class EditProductForm(ProductForm):
    pass


class ReviewForm(BoostrapFormMixin, forms.ModelForm):
    product_pk = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Review
        exclude = ('product',)

    def save(self, commit=True):
        product_pk = self.cleaned_data['product_pk']
        product = Product.objects.get(pk=product_pk)
        review = Review(
            name=self.cleaned_data['name'],
            text=self.cleaned_data['text'],
            rating=self.cleaned_data['rating'],
            product=product,
        )
        if commit:
            review.save()

        return review