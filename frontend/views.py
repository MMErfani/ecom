from django.shortcuts import render
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
