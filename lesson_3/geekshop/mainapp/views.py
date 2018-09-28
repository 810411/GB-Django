from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'главная'},
    {'href': 'catalog', 'name': 'каталог'},
    {'href': 'contact', 'name': 'контакты'},
]


def main(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'главная',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    products = Product.objects.all()[:4]
    content = {
        'title': 'главная',
        'links_menu': links_menu,
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', content)
