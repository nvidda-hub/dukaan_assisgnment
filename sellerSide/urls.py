from sellerSide import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'sellerSide'

urlpatterns = [

    path('', views.sellerHome, name="sellerHome"),
    path('register/', views.register , name="sellerRegister"),
    path('login/', views.login_attempt, name="sellerLogin"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('login_verify_otp/', views.login_otp, name="login_otp"),
    path('inventory/', views.SellerInventoryView.as_view(), name="sellerInventory"),
    path('opened-stores/', views.SellerStoresView.as_view(), name="sellerStores"),
    path('new/store/', views.SellerNewStoreView.as_view(), name="sellerNewStore"),
    path('new/product/', views.SellerNewProductView.as_view(), name="sellerNewProduct"),
    path('profile/', views.SellerProfileView.as_view(), name="sellerProfile"),
    path('logout/', auth_views.LogoutView.as_view(next_page='sellerSide:sellerHome'), name='sellerLogout'),
]