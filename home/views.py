
from django.shortcuts import render,redirect
from .forms import UserAddForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.decorators import unauthenticated_user,admin_only

from adminapp.models import ProductList
# Create your views here.
@admin_only
def homescreen(request):
    product=ProductList.objects.all()
    return render(request,"index.html",{"products":product})

@unauthenticated_user
def Signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("homescreen")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("Signin")


    return render(request,"login.html")


@unauthenticated_user
def Signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("password")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already Taken")
                return redirect("Signup")
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Already Taken")
                return redirect("Signup")
            else:
                new_user = form.save()
                new_user.save()
                messages.info(request,"User Created")
                return redirect("Signin")
  
    return render (request,"register.html",{"form":form})

def signout(request):

    logout(request)
    return redirect("homescreen")