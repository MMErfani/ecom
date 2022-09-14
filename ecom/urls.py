"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from azbankgateways.urls import az_bank_gateways_urls
from peyments.views import go_to_gateway_view, callback_gateway_view
from accounts.views import Register, activate, registerdone, registerfailed

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("register/done/", registerdone, name="registerdone"),
    path("register/failed/", registerdone, name="registerfailed"),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view),
    path('callback-gateway/<int:userid>/<int:amount>/', callback_gateway_view),
    path('', include('frontend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
