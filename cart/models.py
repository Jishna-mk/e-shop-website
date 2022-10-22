
from django.db import models
from django.contrib.auth.models import User
from adminapp.models import ProductList

# Create your models here.
class Cartitems(models.Model):
    CartId=models.AutoField(primary_key=True)
    UserID=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    productID=models.ForeignKey(ProductList,on_delete=models.CASCADE,blank=True,null=True)
    total_items=models.CharField(max_length=180)
