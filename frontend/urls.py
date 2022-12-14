from django.urls import path
from . import views

urlpatterns = [
    path('purchased-products', views.purchased_products, name='purchased_products'),
    path('cart/', views.cart, name='cart'),
    path('my-products/', views.my_products, name='my_products'),
    path('add-to-cart/<int:id>', views.addtocart, name='add-to-cart'),
    path('remove-from-cart/<int:id>', views.removefromcart, name='remove-from-cart'),
    path('products/', views.products, name='product'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/<slug:slug>', views.productPage, name="productPage"),

]
