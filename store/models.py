from calendar import datetime
from distutils.command.upload import upload
from django.utils.html import mark_safe
from email.mime import image
from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=40)
    category=models.ForeignKey("Category",on_delete=models.CASCADE,default=1)
    description=models.TextField(max_length=200,default='',null=True,blank=True)
    specs=models.TextField()
    image=models.ImageField(upload_to='uploads/products/')
    brand=models.ForeignKey("Brand",on_delete=models.CASCADE)
    size=models.ForeignKey("Size",on_delete=models.CASCADE)
    color=models.ForeignKey("Color",on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural='5. product '

    @staticmethod
    def get__products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all__products():
        return Product.objects.all()
    @staticmethod
    def get_all__products_by_ID(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all__products();
    @staticmethod
    def get_all__products_by_brandID(brand_id):
        if brand_id:
            return Product.objects.filter(brand=brand_id)
        else:
            return Product.get_all__products();

class Category(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='uploads/cat/')
    class Meta:
        verbose_name_plural='1. categories '
    def __str__(self):
        return self.name
    @staticmethod
    def get_all__category():
        return Category.objects.all()

class Brand(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='uploads/brand/')
    class Meta:
        verbose_name_plural='2. brand '
    def __str__(self):
        return self.name
    @staticmethod
    def get_all__brand():
        return Brand.objects.all()
class Color(models.Model):
    name=models.CharField(max_length=20)
    color_code=models.CharField(max_length=100)
    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px;background-color:%s"></div>' %(self.color_code))
    class Meta:
        verbose_name_plural='3. colors '
    def __str__(self):
        return self.name

class Size(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='4. size '
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    class Meta:
        verbose_name_plural='7. customer '

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
             return Customer.objects.get(email=email)
        except:
            return False
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default='',blank=True)
    phone=models.CharField(max_length=50,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='8. orders '
    def placeorder(self):
        self.save() 

    
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order\
            .objects\
                .filter(customer=customer_id)\
                    .order_by('-date')


       