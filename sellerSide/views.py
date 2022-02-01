from django.shortcuts import render
from django.views import View


# Create your views here.
class SellerHomeView(View):
    def get(self, request):
        return render(request, "seller_home.html")

class SellerLogInView(View):
    def get(self, request):
        return render(request, "seller_login.html")

class SellerRegistrationView(View):
    def get(self, request):
        return render(request, "seller_registration.html")

class SellerOTPView(View):
    def get(self, request):
        return render(request, "otp.html")

class SellerInventoryView(View):
    def get(self, request):
        return render(request, "seller_inventory.html")

class SellerStoresView(View):
    def get(self, request):
        return render(request, "seller_stores.html")

class SellerNewStoreView(View):
    def get(self, request):
        return render(request, "seller_new_store.html")

class SellerNewProductView(View):
    def get(self, request):
        return render(request, "seller_new_product.html")

class SellerProfileView(View):
    def get(self, request):
        return render(request, "seller_profile.html")
