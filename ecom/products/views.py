from django.shortcuts import render, redirect

from ecom.products.forms import CreateProductForm, EditProductForm
from ecom.products.models import Product


def list_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/list_products.html', context)


def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list products')
    else:
        form = CreateProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/create_product.html', context)


def details_of_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/details_of_product.html', context)


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