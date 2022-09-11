from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Brand_list, Index,Signup,Login, filter_data,logout,Checkout,Orders,search,Brand_list,category,product_detail,add_to_cart,cart_list
urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('signup',Signup.as_view(),name='signup'),
    path('product/<int:id>',product_detail,name='product-detail'),
    path('logout',logout,name='logout'),
    path('search',search,name='search'),
    path('search',search,name='search'),
    path('search',search,name='search'),
    # path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout'),
    path('order',Orders.as_view(),name='order'),
    path('brand',Brand_list,name='brand'),
    path('category',category,name='category'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('filter-data',filter_data,name='filter_data'),
    path('cart',cart_list,name='cart'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
