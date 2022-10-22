
from django.urls import path
from.import views

urlpatterns = [
    path("adminscreen",views.adminscreen,name="adminscreen"),
    path("products",views.products,name="products"),
    path("Product_add",views.Product_add,name="Product_add"),
    path("product_delete",views.product_delete,name="product_delete"),
    path("delete_item/<int:pk>",views.delete_item,name="delete_item"),
    path("product_update",views.product_update,name="product_update"),
    path("product_updatepage/<int:pid>",views.product_updatepage,name="product_updatepage"),
    path("view_product",views.view_product,name="view_product"),

]