from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    product_price = models.IntegerField()
    product_date = models.DateField()
    def __str__(self):
        return self.name
class Buyer(models.Model):
     buyer_name = models.CharField(max_length=50)
     buyer_item = models.CharField(max_length=50)
     buyer_cost = models.CharField(max_length=50)
     buyer_date = models.DateField()
class Seller(models.Model):
     seller_name = models.CharField(max_length=50)
     seller_item = models.CharField(max_length=50)
     seller_cost = models.CharField(max_length=50)
     seller_date = models.DateField()

     def __str__(self):
         return self.seller_name

class Order(models.Model):
    order_seller = models.CharField(max_length=100,null=True)
    order_name = models.CharField(max_length=100,null=True)
    order_quantity = models.CharField(max_length=100, null=True)
    order_cost = models.IntegerField(null=True, blank=True)
    order_date = models.DateField(null=True)
