from django.shortcuts import redirect, render
from django.views import View
from .models import Account
from django.contrib.auth.models import User
import random
from .send_otp_Django import sendOTP



# Create your views here.
class SellerHomeView(View):
    def get(self, request):
        return render(request, "seller_home.html")

class SellerLogInView(View):
    def get(self, request):
        return render(request, "seller_login.html")

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")

        check_accounts = Account.objects.filter(mobile=mobile).first()
        check_users = Account.objects.filter(mobile=mobile).first()

        if check_accounts or check_users:
            context = {"message":"User already exist with this email or mobile number", "class":"danger"}
            return render(request, 'seller_registration.html', context)

        user = User(email=email, first_name=name)
        user.save()

        # generating OTP
        otp = str(random.randint(100000, 999999))

        profile = Account(user=user, mobile=mobile, otp=otp)
        profile.save()
        sendOTP(mobile, otp)

        # creating session for user mobile number for OTP verification
        request.session["mobile"] = mobile
        return redirect('sellerSide:verify_otp') # calling below otp function

    return render(request, 'seller_registration.html')


def verify_otp(request):
    # getting data from session
    mobile = request.session["mobile"]
    context = {'mobile':mobile}
    if request.method == "POST":
        otp = request.POST.get("otp")
        profile = Account.objects.filter(mobile=mobile).first()
        if otp == profile.otp:
            return redirect('sellerSide:sellerHome')
        else:
            context = {"message":"send OTP again", "class":"danger", 'mobile':mobile}
            return render(request, 'otp.html', context)
    return render(request, 'otp.html')

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
