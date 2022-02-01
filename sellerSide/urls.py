from sellerSide import views
from django.urls import path

app_name = 'sellerSide'

urlpatterns = [

    path('', views.SellerHomeView.as_view(), name="sellerHome"),
    path('signin/', views.SellerSignInView.as_view(), name="sellerAuth"),
    path('inventory/', views.SellerInventoryView.as_view(), name="sellerInventory"),
    path('opened-stores/', views.SellerStoresView.as_view(), name="sellerStores"),
    path('new/store/', views.SellerNewStoreView.as_view(), name="sellerNewStore"),
    path('new/product/', views.SellerNewProductView.as_view(), name="sellerNewProduct"),
    path('profile/', views.SellerProfileView.as_view(), name="sellerProfile"),

]