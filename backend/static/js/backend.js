$(function(){
    //判断二级导航 option个数 是否为真，也就是 有三级导航
	if($('#secondMenu option').length){
	 $('.secondMenu').css('display','block');
	}else{
		 $('.secondMenu').css('display','none');
	}
	 //判断三级导航 option个数 是否为真，也就是 有三级导航
	if($('#thirdMenu option').length){
	 $('.thirdMenu').css('display','block');
	}else{
		 $('.thirdMenu').css('display','none');
	}
    selectMenu();
});
//二级 导航 联动
function selectMenu(){
	$('#parentMenu').change(function(){
			  $.ajax({
			         url: "/backend/Twolink/",
			         type: "POST",
			         data: {id:$(this).val()},
			         dataType: "json",
			         success: function(data){
			         	 if(data=='error')
			         	 {   
			         	 	  //没有二级导航
			                 $('.secondMenu').css('display','none');
			         	 }
			         	 else{  
			         	 	       //有二级导航
			                     $('.secondMenu').css('display','block');
			         	 	     $('#secondMenu').html('');
			         	 	     var option='';
			         	 	     for(var i=0;i<data.length;i++)
			         	 	     {
			         	 	     	var value=data[i]['id'];
			                        option = '<option value='+value+'>' + data[i]['name'] + 
			                             '</option>';     
			                                // console.log(data[i]);
			                         $('#secondMenu').append(option);
			                         option='';
			         	 	     }    
			         	 	    
			         	 	   var len=$('#secondMenu').find("option").length;
				         	 	    if (len<1)
				         	 	       {
				         	 	           $('#secondMenu').attr('disabled',true);
				         	 	       }
				         	 	    else{
				         	 	    	  $('#secondMenu').attr('disabled',false);
				         	 	        }
			                  }  
			           }  
			     });
   });
    //三级 联动
   $('#secondMenu').change(function(){
		   $.ajax({
			         url: "/backend/Twolink/",
			         type: "POST",
			         data: {id:$(this).val()},
			         dataType: "json",
			         success: function(data){
			         	 if(data=='error')
			         	 {
			                 //没有三级导航
			                  $('.thirdMenu').css('display','none');
			         	 }
			         	 else{   
			         	 	    //有三级导航
			         	 	    $('.thirdMenu').css('display','block');
			         	 	     $('#thirdMenu').html('');
			         	 	     var option='';
			         	 	     for(var i=0;i<data.length;i++)
			         	 	     {
			         	 	     	var value=data[i]['id'];
			                        option = '<option value='+value+'>' + data[i]['name'] + 
			                             '</option>';     
			                                // console.log(data[i]);
			                         $('#thirdMenu').append(option);
			                         option='';
			         	 	     }    
			         	 	    
			         	 	   var len=$('#thirdMenu').find("option").length;
				         	 	    if (len<1)
				         	 	       {
				         	 	           $('#thirdMenu').attr('disabled',true);
				         	 	            $('#thirdMenu').css('display','none');
				         	 	       }
				         	 	    else{
				         	 	    	  $('#thirdMenu').attr('disabled',false);
				         	 	        }
			                  }  
			           }  
			     });
    });

}