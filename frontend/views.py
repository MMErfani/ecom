from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
    
def products(request):
    products = Product.objects.all()
    return render(request, 'frontend/products.html', {'products':products})

def product(request):
    products = Product.objects.all()
    return render(request, 'frontend/product.html', {'products':products})

def index(request):
    products = Product.objects.all()
    return render(request, 'frontend/index.html', {'products':products})

def about(request):
    products = Product.objects.all()
    return render(request, 'frontend/about.html', {'products':products})

def contact(request):
    products = Product.objects.all()
    return render(request, 'frontend/contact.html', {'products':products})

def productPage(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'frontend/product.html', context = {'pruduct' : product})
