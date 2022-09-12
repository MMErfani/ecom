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
    products = Product.objects.filter(status='published')
    return render(request, 'frontend/index.html', {'products':products})

def cart(request):
    cart = Cart.objects.get(user=request.user)
    ids = [pro.pid for pro in cart.pids.all()]
    total=sum([pro.price for pro in cart.pids.all()])
    products = [Product.objects.get(pid=id) for id in ids]
    return render(request, 'frontend/cart.html', {'products':products, 'total':total})
    
def about(request):
    products = Product.objects.all()
    return render(request, 'frontend/about.html', {'products':products})

def contact(request):
    products = Product.objects.all()
    return render(request, 'frontend/contact.html', {'products':products})

def productPage(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'frontend/product.html', context = {'productdetail' : product})
