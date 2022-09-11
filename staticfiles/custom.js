$(document).ready(function(){
   $(".choose-size").hide();
   $(".choose-color").on('click', function(){
    var _color=$(this).attr('data-color');
    $(".choose-size").hide();
    $(".color"+_color).show();
    $(".color"+_color).first().addClass('active');
   });
   
   $(".choose-size").on('click',function(){
		$(".choose-size").removeClass('active');
		$(this).addClass('active');

		var _price=$(this).attr('data-price');
		$(".product-price").text(_price);
	})
   var _color=$(".choose-color").first().attr('data-color');
   var _price=$(".choose-size").first().attr('data-price');

   $(".color"+_color).show();
   $(".color"+_color).first().addClass('active');
	$(".product-price").text(_price);

   $("#addToCartBtn").on('click', function(){
      var _qty=$("#productQty").val();
      var _productId=$(".product-id").val();
      var _productName=$(".product-name").val();
      console.log(_qty,_productName,_productId);

   });

});