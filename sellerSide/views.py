from django.shortcuts import redirect, render
from django.views import View
from .models import Account
from django.contrib.auth.models import User
import random
from .send_otp_Django import sendOTP
from django.contrib.auth import authenticate, login



# Create your views here.

def sellerHome(request):
    return render(request, "seller_home.html")

def login_attempt(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        
        user = Account.objects.filter(mobile = mobile).first()
        print("mobile-------------------->")
        if user is None:
            context = {'message' : 'User not found' , 'class' : 'danger' }
            return render(request,'seller_login.html' , context)
        
        otp = str(random.randint(1000 , 9999))
        user.otp = otp
        user.save()
        sendOTP(mobile , otp)
        request.session['mobile'] = mobile
        return redirect('sellerSide:login_otp')        
    return render(request,'seller_login.html')


def login_otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    print("login_otp is called")
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Account.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            user = User.objects.get(id = profile.user.id)
            login(request , user)
            return redirect('sellerSide:sellerHome')
        else:
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile }
            return render(request,'seller_login_otp.html' , context)
    
    return render(request,'seller_login_otp.html' , context)

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