from django.shortcuts import render

from shop.models import Product


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()

    return render(request, 'shop/home.html')