from django.urls import path
import mainapp.views as mainapp


urlpatterns = [
	path('', mainapp.main, name='main'),
	path('catalog/', mainapp.catalog, name='catalog'),
	path('contact/', mainapp.contact, name='contact'),
]
