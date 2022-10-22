from itertools import product
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import ProductListForm
from django.contrib import messages
from .decorator import admin_authenticated
from .models import ProductList
# Create your views here.


def adminscreen(request):

    return render(request, "admin.html")


@admin_authenticated
def products(request):

    return render(request, "product_admin.html")


@admin_authenticated
def Product_add(request):
    form = ProductListForm()

    if request.method == 'POST':
        form = ProductListForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save()
            form_data.save()
            messages.info(request, "Product added to list")
            return redirect('Product_add')
        else:
            form = ProductListForm()
            messages.info(request, "Not Done")
            return redirect('Product_add')

    return render(request, "product.html", {'form': form})


def product_delete(request):

    products = ProductList.objects.all()
    if request.method == "POST":
        id = request.POST["id"]
        product = ProductList.objects.get(Product_ID=id)
        product.delete()
        messages.info(request, "Product Deleted!")
        return redirect("product_delete")

    return render(request, "product_delete.html", {"products": products})


def delete_item(request, pk):
    item = ProductList.objects.get(Product_ID=pk)
    item.delete()
    messages.info(request, "product deleted")
    return redirect("product_delete")


def product_update(request):

    products = ProductList.objects.all()
    if request.method == "POST":
        id = request.POST["id"]
        return redirect("product_updatepage/"+id)

    return render(request, "product_update.html", {"products": products})


def product_updatepage(request, pid):
    product = ProductList.objects.get(Product_ID=pid)
    if request.method == "POST":
        ProductList.objects.filter(Product_ID=pid).update(Product_Name=request.POST["Product_Name"],Product_Catogary=request.POST["Product_Catogary"],Product_Discription=request.POST["Product_Discription"],Product_Price=request.POST["Product_Price"])
        return redirect("adminscreen")

    return render(request, "product_updatepage.html", {"product": product})

def view_product(request):
    products = ProductList.objects.all()
    return render(request,"view_product.html",{"products":products})