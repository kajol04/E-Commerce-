from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import Brand_list, Index,Signup,Login, filter_data,logout,search,Brand_list,category,product_detail,add_to_cart,cart_list,delete_cart_item,update_cart_item,checkout,payment_done,payment_cancelled
urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('signup',Signup.as_view(),name='signup'),
    path('product/<int:id>',product_detail,name='product-detail'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('search',search,name='search'),
    path('brand',Brand_list,name='brand'),
    path('category',category,name='category'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('filter-data',filter_data,name='filter_data'),
    path('cart',cart_list,name='cart'),
    path('delete-from-cart',delete_cart_item,name='delete-from-cart'),
    path('update-to-cart',update_cart_item,name='update-to-cart'),
    path('checkout',checkout,name='checkout'),
     path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_cancelled, name='payment_cancelled'),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
