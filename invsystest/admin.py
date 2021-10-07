from django.contrib import admin

# Register your models here.
from.models import Product
admin.site.register(Product)
from.models import Buyer
admin.site.register(Buyer)
from.models import Seller
admin.site.register(Seller)
from.models import Order
admin.site.register(Order)