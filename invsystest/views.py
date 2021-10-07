
from django.shortcuts import render
from .models import Product
from .models import Buyer
from .models import Seller
from .models import Order
from django.http import HttpResponse
# Create your views here.


def index(request):
    products = Product.objects.all()
    prod_count = Product.objects.all().count()
    buy_count = Buyer.objects.all().count()
    sell_count = Seller.objects.all().count()
    ord_count = Order.objects.all().count()

    print(products)

    params = {'product' : products, 'numberofp' : prod_count, 'numberofs': sell_count,'numberofb' : buy_count, 'numberofo': ord_count}
    return render(request, 'index.html', params)
def buyer1(request):
    buyer = Buyer.objects.all()
    buy_count = Buyer.objects.all().count()
    sell_count = Seller.objects.all().count()
    ord_count = Order.objects.all().count()
    prod_count = Product.objects.all().count()
    print(buyer)
    params = {'buyer' : buyer, 'numberofb' : buy_count, 'numberofs': sell_count, 'numberofp' : prod_count, 'numberofo': ord_count}
    return render(request, 'buyer.html', params)
def seller1(request):
    seller = Seller.objects.all()
    sell_count = Seller.objects.all().count()
    buy_count = Buyer.objects.all().count()
    ord_count = Order.objects.all().count()
    prod_count = Product.objects.all().count()
    print(seller)

    params = {'seller': seller, 'numberofs': sell_count,'numberofb' : buy_count, 'numberofp' : prod_count,'numberofo': ord_count}
    return render(request, 'seller.html', params)
def order1(request):
 order = Order.objects.all()
 ord_count = Order.objects.all().count()
 sell_count = Seller.objects.all().count()
 buy_count = Buyer.objects.all().count()
 prod_count = Product.objects.all().count()

 params = {'order': order, 'numberofo': ord_count, 'numberofs': sell_count,'numberofb' : buy_count, 'numberofo': ord_count, 'numberofp' : prod_count }
 return render(request, 'order.html', params)

def buyerform1(request):
    if request.method == "POST":
        buyname = request.POST['buyname']
        buyitem = request.POST['buyitem']
        buycost = request.POST['buycost']
        buydate = request.POST['buydate']
        #print(buyname, buyitem, buycost, buydate)
        ins = Buyer(buyer_name=buyname, buyer_item=buyitem, buyer_cost=buycost, buyer_date=buydate)
        ins.save()
    return render(request, 'buyer_form.html')
def sellerform1(request):

    if request.method == "POST":
        sn = request.POST['sn']
        sellitem = request.POST['sellitem']
        sellcost = request.POST['sellcost']
        sd = request.POST['sd']
        ins = Seller(seller_name=sn, seller_item=sellitem, seller_cost=sellcost, seller_date=sd)
        ins.save()
    return render(request, 'seller_form.html')
def productform1(request):

    if request.method == "POST":
        prodname= request.POST['prodname']
        prodquan = request.POST['prodquan']
        prodcost = request.POST['prodcost']
        proddate = request.POST['proddate']
        ins = Product(product_name=prodname, product_quantity=prodquan, product_price=prodcost, product_date=proddate)
        ins.save()
    return render(request, 'product_add.html')
def orderform1(request):
    products = Product.objects.all()
    seller = Seller.objects.all()

    if request.method == "POST":
        Check = request.POST.getlist('checking')
        quan = request.POST.getlist('quan')
        ssl = request.POST.get('ssl')
        orddate = request.POST['orddate']
        ordcost = request.POST['ordcost']
        # concurrent list
        newQuan = []

        for q in quan:
            if q:
                newQuan.append(q)
            else:
                continue

        for qu, n in zip(newQuan, Check):
            Order.objects.create(order_name=n, order_quantity=qu, order_seller = ssl, order_date = orddate, order_cost = ordcost)
            prod_obj = Product.objects.filter(name=n).first()
            prod_obj.quantity = int(prod_obj.quantity) - int(qu)
            prod_obj.save()


    params = {'product': products, 'seller': seller}
    return render(request,'order_form.html',params)
def bill(request):
    order = Order.objects.all()
    params = {'order':order}
    return render(request, 'bill.html',params)