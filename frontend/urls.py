from django.urls import path
from . import views

urlpatterns = [

    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>', views.addtocart, name='add-to-cart'),
    path('remove-from-cart/<int:id>', views.removefromcart, name='remove-from-cart'),
    path('product/', views.product, name='product'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<slug:slug>', views.productPage, name="productPage"),

]
