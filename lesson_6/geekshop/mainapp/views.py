from django.http import HttpResponseBadRequest
from django.shortcuts import render
from basketapp.models import Basket
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
import random

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'главная'},
    {'href': 'catalog', 'name': 'магазин'},
    {'href': 'contact', 'name': 'контакты'},
]

def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def getHotProduct():
    products = Product.objects.all()
    return random.sample(list(products), 4)


def main(request):
    hot_product = getHotProduct()
    content = {
        'title': 'главная',
        'links_menu': links_menu,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):
    title = 'магазин'
    catalog_menu = ProductCategory.objects.all()
    basket = getBasket(request.user)

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
        'basket': basket,
    }
    return render(request, 'mainapp/catalog.html', content)


def product(request, pk=None):
    basket = getBasket(request.user)
    title = get_object_or_404(Product, id=pk).name
    product_ = get_object_or_404(Product, id=pk)
    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product_,
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', content)
