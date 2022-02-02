from django.db import models
from django.contrib.auth.models import User
import random



# Create your models here.

random_string = "!@#$%^&(){}<>?'+_"

class Account(models.Model):
    userid = models.AutoField(primary_key=True, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=30)
    otp = models.CharField(max_length=6)

    @property
    def issued_token_to_user(self):
        return f"USR_token_{random.shuffle(random_string)}&&{self.mobile[:3]}"

    def __str__(self):
        return f" {self.user}, user is created"


class Store(models.Model):
    storeid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Account, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=20)
    store_city = models.CharField(max_length=30)
    store_state = models.CharField(max_length=30)
    store_pincode = models.CharField(max_length=30)
    
    @property
    def store_link(self):
        return f"{self.store_name}_&_{random.shuffle(random_string)}"
    
    def __str__(self):
        return f"Store created with name {self.store_name}"



class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    product_desc = models.TextField()
    product_mrp = models.FloatField()
    product_salePrice = models.FloatField()
    product_image = models.ImageField(upload_to="product_images")
    product_cat = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"product {self.product_name}"


# class Categories(models.Model):
#     id = models.AutoField(primary_key=True)
#     product_name = models.ForeignKey(Product, on_delete=models.CASCADE)


class Customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    customer_mobile = models.CharField(max_length=13, unique=True)
    customer_name = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=30)
    customer_state = models.CharField(max_length=30)
    customer_pincode = models.CharField(max_length=30)

    def __str__(self):
        return f"customer with name {self.customer_name}"


class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_mobile = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"order details for customer mobile {self.customer_mobile} with {self.product_name}"