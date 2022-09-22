from itertools import product
from django.contrib import admin
from .models import Product,Category,Customer,Order,Color,Brand,Size,ProductAttribute
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['id','name','category','brand','status']
    list_editable=('status',)
   
class AdminProductAttribute(admin.ModelAdmin):
    list_display=('id','product','price','color','size')

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminColor(admin.ModelAdmin):
    list_display=['name','color_bg']

admin.site.register(Product,AdminProduct)
admin.site.register(ProductAttribute,AdminProductAttribute)

admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Color,AdminColor)
admin.site.register(Order)
admin.site.register(Size)



