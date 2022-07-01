from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Brand_list, Index,Signup,Login,logout,Checkout,Cart,Orders,search,Brand_list,category,product_detail

urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('signup',Signup.as_view(),name='signup'),
    path('product/<int:id>',product_detail,name='product-detail'),
    
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('search',search,name='search'),
    path('search',search,name='search'),
    path('search',search,name='search'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout'),
    path('order',Orders.as_view(),name='order'),
    path('brand',Brand_list,name='brand'),
    path('category',category,name='category'),





] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
