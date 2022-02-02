from django.contrib import admin
from sellerSide.models import Account, Product, Customer, Order, Store
# Register your models here.


@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ["userid", "user", "mobile", "otp"]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["productid", "product_name", "product_desc", "product_mrp", "product_salePrice", "product_image", "product_cat"]


@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ["storeid", "userid", "store_name", "store_city", "store_state", "store_pincode"]


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["customerid", "customer_mobile", "customer_city", "customer_state", "customer_pincode"]


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["orderid", "productid", "customer_mobile"]
