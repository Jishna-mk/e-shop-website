from django.db import models

# Create your models here
class ProductList(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=200)
    Product_Catogary = models.CharField(max_length=200)
    Product_Discription = models.CharField(max_length=1000)
    Product_Price = models.CharField(max_length=100)
    Product_Image = models.ImageField(upload_to = "product_image")