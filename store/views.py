import json 
from os import remove
from turtle import title
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.views import View
from .models import Product,Category,Customer,Order,Brand,Size,ProductAttribute,Color
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator 
from django.template.loader import render_to_string


class Index(View):
    # def post(self,request):
    #     product=request.POST.get('product')
    #     remove=request.POST.get('remove')
        # cart=request.session.get('cart')
        # if cart:
        #     quantity=cart.get(product)
        #     if quantity:
        #         if remove:
        #             if quantity <=1:
        #                 cart.pop(product)
        #             else:
        #                 cart[product]=quantity-1
        #         else:
        #             cart[product]=quantity+1
        #     else:
        #         cart[product]=1
        # else:
        #     cart={}
        #     cart[product]=1
        # request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        # return redirect('home')
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        product=None
        
        name=request.session.get('customer_name')
        categories=Category.get_all__category()
        categoryid=request.GET.get('category')
        brandlist=Brand.get_all__brand()
        brandid=request.GET.get('brand')
        if categoryid:
                product=Product.get_all__products_by_ID(categoryid)
        elif brandid:
            product=Product.get_all__products_by_brandID(brandid)
        else:
            product=Product.get_all__products()
        context = {
            "product": product,
            "category":categories,
            "brandlist":brandlist,
            "name":name,
            
        }
        return render(request,'index.html',context)
   
def Brand_list(request):
    brands=Brand.get_all__brand()
    data = {
            "data":brands,
        }
    return render(request,'brand.html',data)

def category(request):
    categories=Category.get_all__category()
    data = {
            "data":categories,
        }
    return render(request,'category.html',data)


class Signup(View):
    def get(self,request):
        return render(request,'registration/signup.html')

    def post(self,request):
        data= request.POST
        first_name=data.get('firstname')
        last_name=data.get('lastname')
        email=data.get('email')
        password=data.get('password')
        phone=data.get('phone')
        #validation
        value={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone
        }
        error_message=None
        customer=Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password,
            )
        error_message=self.ValidateCustomer(customer)
     #saving
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            context={
                'error':error_message,
                'values':value
            }
            return render(request,'registration/signup.html',context)

    def ValidateCustomer(self,customer):
        error_message=None
        if(not customer.first_name):
            error_message="First name required!!!"
        elif len(customer.first_name)<4:
            error_message="First name must be 4 character long or more"
        elif not customer.last_name:
            error_message="Last name required!!!"
        elif len(customer.last_name)<4:
            error_message="Last name must be 4 character long or more"
        elif not customer.phone:
            error_message="Phone Number required!!!"
        elif len(customer.phone)<10:
            error_message="Phone Number must be 10 character long"
        elif len(customer.email)<5:
            error_message="Email must be 5 character long"
        elif len(customer.password)<6:
            error_message="Password must be 6 character long"
        elif customer.isExists():
            error_message="Email Already Registered"
        return error_message

class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'registration/login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer']=customer.id 
                request.session['customer_name']=customer.first_name
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('home')
            else:
                error_message='Email Or Password Invalid!!!'
        else:
            error_message='Email Or Password Invalid!!!'

        return render(request,'registration/login.html',{'error':error_message})

def logout(request):
    request.session.clear()
    return redirect('login')


class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get__products_by_id(list(cart.keys()))
        for product in products:
            order=Order(customer=Customer(id=customer),
            product=product,
            price=product.price,
            address=address,
            phone=phone,
            quantity=cart.get(str(product.id)))
            order.placeorder();
        request.session['cart']={}
        return redirect('cart')

class Orders(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_order_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})

def search(request):
    q=request.GET['q']
    data=Product.objects.filter(name__icontains=q)   
    return render(request,'search.html',{'data':data})   


def product_detail(request,id):
    
    product=Product.objects.get(id=id)
    colors=ProductAttribute.objects.filter(product=product).values('color__name','color__id','color__color_code').distinct()
    sizes=ProductAttribute.objects.filter(product=product).values('size__name','size__id','color__id','price').distinct()
    context={
        'product':product,
        'colors':colors,
        'sizes':sizes
    }
    return render(request,'product-detail.html',context)

def filter_data(request):
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	brands=request.GET.getlist('brand[]')
	
	allProducts=Product.objects.all().order_by('-id').distinct()
    
	if len(colors)>0:
		allProducts=allProducts.filter(productattribute__color__id__in=colors).distinct()
                       
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(brands)>0:
		allProducts=allProducts.filter(brand__id__in=brands).distinct()
	t=render_to_string('ajax/product-list.html',{'product':allProducts})
	return JsonResponse({'data':t}) 

def add_to_cart(request):
    cart_p={}
    cart_p[str(request.GET['id'])]={
        'name':request.GET['name'],
        'price':request.GET['price'],
        'qty':request.GET['qty'],}    
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata']=cart_data
        else:
            cart_data=request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata']=cart_data

    else:
        request.session['cartdata']=cart_p 
    return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])}) 
                
def cart_list(request):
    return render(request,'cart.html')
        
    