from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.products, name='products'),
    path('product/', views.product, name='product'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<slug:slug>', views.productPage, name="productPage"),

]
