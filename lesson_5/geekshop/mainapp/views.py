from django.http import HttpResponseBadRequest
from django.shortcuts import render
from basketapp.models import Basket
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'главная'},
    {'href': 'catalog', 'name': 'каталог'},
    {'href': 'contact', 'name': 'контакты'},
]


def main(request):
    content = {
        'title': 'главная',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):
    title = 'каталог'
    catalog_menu = ProductCategory.objects.all()

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'catalog_menu': catalog_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/catalog.html', content)

    products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'catalog_menu': catalog_menu,
        'products': products,
        'category': {'name': 'все'},
    }
    return render(request, 'mainapp/catalog.html', content)


def product(request, pk=None):
    basket = []
    product_in_basket = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for item in basket:
            product_in_basket += item.quantity

    title = get_object_or_404(Product, id=pk).name
    product_ = get_object_or_404(Product, id=pk)
    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product_,
        'basket': basket,
        'product_in_basket': product_in_basket,
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', content)
