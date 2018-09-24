from django.shortcuts import render
import json

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


def catalog(request):
    storegrid = []
    json_data = open('mainapp/static/database/data.json', encoding='utf-8')
    storegrid = json.load(json_data)

    content = {
        'title': 'каталог',
        'links_menu': links_menu,
        'storegrid': storegrid
    }
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    content = {
        'title': 'контакты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', content)
