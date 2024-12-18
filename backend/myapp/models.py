from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=15)

class cart(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_quantity=models.IntegerField()
    bill=models.IntegerField()

# class admin(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     password=models.CharField(max_length=15)

# class product(models.Model):
#     product_name=models.CharField(max_length=50)
#     product_price=models.IntegerField()
#     product_category=models.CharField(max_length=50)
#     product_stock=models.IntegerField()

class buy(models.Model):
    buy_name=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    pincode=models.CharField(max_length=6)
    card_no=models.CharField(max_length=15)
    paid=models.CharField(max_length=20)
