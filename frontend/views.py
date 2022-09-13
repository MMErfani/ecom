from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
    
def products(request):
    products = Product.objects.filter(status='published')
    return render(request, 'frontend/products.html', {'products':products})


def index(request):
    products = Product.objects.filter(status='published')
    return render(request, 'frontend/index.html', {'products':products})

def cart(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            ids = [pro.pid for pro in cart.pids.filter(status="published")]
            total=sum([pro.price for pro in cart.pids.filter(status="published")])
            products = [Product.objects.get(pid=id) for id in ids]
            print(str(products))
            if products!=[]:
                text= "پرداخت"
                link="#"
            else:
                text= "بریم به آخرین محصولات سر بزنیم"
                link="/products"
        except:
            cart = Cart(user=request.user)
            cart.save()
            total = 0
            products = []
            text= "بریم به آخرین محصولات سر بزنیم"
            link="/products"
    else:
       total = 0
       products = []
       text= "ورود"
       link="/login"
    

    return render(request, 'frontend/cart.html', {'products':products, 'total':total, 'link':link, 'text':text})

def addtocart(request, id):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
        except:
            cart = Cart(user=request.user)
            cart.save()
        ids = [pro.pid for pro in cart.pids.all()]     
        if id not in ids:
            c = cart.pids.add(Product.objects.get(pid=id))
            cart.save()
    return redirect('/cart/')
    
def removefromcart(request, id):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            ids = [pro.pid for pro in cart.pids.all()]
            if id in ids:
                c = cart.pids.remove(Product.objects.get(pid=id))
                cart.save()
        except:
            cart = Cart(user=request.user)
            cart.save()
    return redirect('/cart/')
    
def about(request):
    products = Product.objects.all()
    return render(request, 'frontend/about.html', {'products':products})

def contact(request):
    products = Product.objects.all()
    return render(request, 'frontend/contact.html', {'products':products})

def productPage(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if str(product.status)=='draft':
        text="فروش این محصول متوقف شده است"
        link="#"
    elif str(product.status)=='published':
        try:
            cart = Cart.objects.get(user=request.user)
            ids = [pro.pid for pro in cart.pids.all()]
 
            if product.pid in ids:
                text="این محصول در سبد خرید موجود است. (نمایش)"
                link="/cart"
            else:
                text="افزودن به سبد خرید"
                link=f"/add-to-cart/{product.pid}"
        except:
            if request.user.is_authenticated:
                text="افزودن به سبد خرید"
                link=f"/add-to-cart/{product.pid}"
            else:
                text= "برای خرید محصول ابتدا وارد حساب کاربری شوید"
                link="/login"   
        

    return render(request, 'frontend/product.html', context = {'productdetail' : product, 'link':link, 'text':text})
