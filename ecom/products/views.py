from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ecom.products.forms import CreateProductForm, EditProductForm, ReviewForm
from ecom.products.models import Product, Review


def list_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/list_products.html', context)


@login_required()
def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('list products')
    else:
        form = CreateProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/create_product.html', context)


def details_of_product(request, pk):
    product = Product.objects.get(pk=pk)
    is_owner = product.user == request.user
    context = {
        'product': product,
        'reviews': product.review_set.all(),
        'review_form': ReviewForm(
            initial={
                'product_pk': pk,
            }
        ),
        'is_owner': is_owner,
    }
    return render(request, 'products/details_of_product.html', context)


@login_required()
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list products')
    else:
        form = EditProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required()
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if product.image:
            product.image.delete()
        product.delete()
        return redirect('list products')
    else:
        context = {
            'product': product,
        }

        return render(request, 'products/delete_product.html', context)


@login_required()
def review_product(request, pk):
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user
        review.save()
    return redirect('details of product', pk)

