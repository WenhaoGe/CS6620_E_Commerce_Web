from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from products.models import Product
from .forms import ProductForm


def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def edit_product(request, pk):

    # product = get_object_or_404(Product, pk = pk)
    #
    # new_product = Product(request.POST or None, instance = product)
    #
    # if new_product.is_valid():
    #     new_product.save()
    #     return HttpResponseRedirect("/" + pk)
    #
    # context = {
    #     'product': product
    # }

    return render(request, 'product_index.html', {})


def create_product(request):

    if request.method == "POST":
        product_form = ProductForm(data=request.POST)
        if product_form.is_valid():
            product_form = product_form.save()
            return HttpResponseRedirect("/")
    else:
        product_form = ProductForm()

    return render(request, "create_product.html", {"product": product_form})


def delete_product(request, id):
    pass