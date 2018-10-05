from django.urls import path
from django.conf.urls import url
import mainapp.views as mainapp


urlpatterns = [
	path('', mainapp.main, name='main'),
	path('catalog/', mainapp.catalog, name='catalog'),
	path('contact/', mainapp.contact, name='contact'),
	path('catalog/<pk>/', mainapp.catalog, name='catalog'),
	path('product/<pk>', mainapp.product, name='product'),
]
