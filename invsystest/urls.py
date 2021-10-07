"""isproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("Buyer", views.buyer1, name="buyer"),
    path("seller", views.seller1, name="seller"),
    path("order", views.order1, name="order"),
    path("buyerform", views.buyerform1, name="buyerform"),
    path("sellerform", views.sellerform1, name="sellerform"),
    path("productform", views.productform1, name="productform"),
    path("orderform", views.orderform1, name="orderform"),
    path("bill", views.bill, name="bill")

]
