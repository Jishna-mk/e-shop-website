from django.urls import path
from .import views

urlpatterns = [
    path("",views.homescreen,name="homescreen"),
    path("Signin",views.Signin,name="Signin"),
    path("Signup",views.Signup,name="Signup"),
    path("signout",views.signout,name="signout")
]
