from .models import Product,ProductAttribute
def get_filters(request):
	cats=Product.objects.distinct().values('category__name','category__id')
	brands=Product.objects.distinct().values('brand__name','brand__id')
	colors=ProductAttribute.objects.distinct().values('color__name','color__id','color__color_code')
	
	data={
		'cats':cats,
		'brands':brands,
		'colors':colors,
		
	}
	return data