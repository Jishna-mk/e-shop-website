from email.errors import NonPrintableDefect
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group==None:
            return view_func(request,*args, **kwargs)
        if group=="customer":
            return view_func(request,*args,**kwargs)
        if group=="admin":
            return redirect('adminscreen')
    return  wrapper_function

def unauthenticated_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_function

