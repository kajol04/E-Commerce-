$(document).ready(function(){
   $(".choose-size").hide();
   $(".choose-color").on('click', function(){
      $(".choose-color").removeClass('focused');
		$(this).addClass('focused');

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
   $(".choose-color").first().addClass('focused')
   var _color=$(".choose-color").first().attr('data-color');
   var _price=$(".choose-size").first().attr('data-price');

   $(".color"+_color).show();
   $(".color"+_color).first().addClass('active');
	$(".product-price").text(_price);

   $(document).on('click', "#addToCartBtn",function(){
      var _vm=$(this);
      var _qty=$("#productQty").val();
      var _productId=$(".product-id").val();
      var _productImage=$(".product-image").val();
      var _productName=$(".product-name").val();
      var _productPrice=$(".product-price").text();
      $.ajax({
         url:'/add-to-cart' ,
         data:{
            'id':_productId,
            'image':_productImage,
            'qty':_qty,
            'name':_productName,
            'price':_productPrice,
         },
         dataType:'json',
         beforeSend:function(){
            _vm.attr('disabled',true);
         },
         success: function(res){
            _vm.attr('disabled',false);
            $(".cart-list").text(res.totalitems);
            // console.log(res);
            
         }
      });

   });

   $(document).on('click', '.delete-item',function(){
      var _pId=$(this).attr('data-item');
      var _vm=$(this);
      $.ajax({
         url:'/delete-from-cart' ,
         data:{
            'id':_pId,
   
         },
         dataType:'json',
         beforeSend:function(){
            _vm.attr('disabled',true);
         },
         success: function(res){
            $(".cart-list").text(res.totalitems);
            _vm.attr('disabled',false);
            $("#cartList").html(res.data);
         }
      });

   });
   $(document).on('click', '.update-item',function(){
      var _pId=$(this).attr('data-item');
      var _pQty=$(".product-qty-"+ _pId).val();
      var _vm=$(this);
      $.ajax({
         url:'/update-to-cart' ,
         data:{
            'id':_pId,
            'qty':_pQty,
         },
         dataType:'json',
         beforeSend:function(){
            _vm.attr('disabled',true);
         },
         success: function(res){
            // $(".cart-list").text(res.totalitems);
            _vm.attr('disabled',false);
            $("#cartList").html(res.data);
         }
      });

   });

});