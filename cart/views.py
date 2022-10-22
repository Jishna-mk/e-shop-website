from itertools import product
from django.shortcuts import render,redirect

from adminapp.models import ProductList
from.models import Cartitems

# Create your views here.
def Cart(request):
    name=[]
    price=[]
    User_id=request.user
    items=Cartitems.objects.filter(UserID=User_id)
    for i in items:
        product =i.productID
        name.append(product.Product_Name)
        price.append(product.Product_Price)
    return render (request,'cart1.html',{'name':name,'price':price})

def CartAdd(request,pk):
    product=ProductList.objects.get(Product_ID=pk)
    new_item=Cartitems.objects.create(UserID=request.user,productID=product,total_items=1)
    new_item.save()
    return redirect("Cart")
