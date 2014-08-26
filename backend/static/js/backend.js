$(function(){
    //判断二级导航 option个数 是否为真，也就是 有二级导航
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
			                 //也没有三级导航
			                 $('.thirdMenu').css('display','none');
			         	 }
			         	 else{  
			         	 	       //有二级导航  data['data'][i]['id'].length
			         	 	       //alert( data['data'].length);
			                     $('.secondMenu').css('display','block');
			         	 	     $('#secondMenu').html('');
			         	 	     var option='';
			         	 	     for(var i=0;i<data['data'].length;i++)
			         	 	     {
			         	 	     	var value=data['data'][i]['id'];
			         	 	     	//console.log()
			                        option = '<option value='+value+'>' + data['data'][i]['name'] + 
			                             '</option>';     
			                                // console.log(data[i]);
			                         $('#secondMenu').append(option);
			                         option='';
			         	 	     }    
			         	 	     //说明有 三级导航  不为空
			         	 	    if (data['data2'] != "")
			         	 	    {
			         	 	    	 //alert(data['data2']);
				         	 	      $('.thirdMenu').css('display','block');
				         	 	      $('#thirdMenu').html('');
				         	 	     var option='';
				         	 	     for(var i=0;i<data['data2'].length;i++)
				         	 	     {
				         	 	     	var value=data['data2'][i]['id'];
				                        option = '<option value='+value+'>' + data['data2'][i]['name'] + 
				                             '</option>';     
				                                // console.log(data[i]);
				                         $('#thirdMenu').append(option);
				                         option='';
				         	 	     }    
			         	 	    }
			         	 	    else{
 									$('.thirdMenu').css('display','none');
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
			         	 	     //说明有 三级导航
			         	 	    if (data['data2'])
			         	 	    {
				         	 	      $('.thirdMenu').css('display','block');
				         	 	      $('#thirdMenu').html('');
				         	 	     var option='';
				         	 	     for(var i=0;i<data['data'].length;i++)
				         	 	     {
				         	 	     	var value=data['data'][i]['id'];
				                        option = '<option value='+value+'>' +data['data'][i]['name'] + 
				                             '</option>';     
				                                // console.log(data[i]);
				                         $('#thirdMenu').append(option);
				                         option='';
				         	 	     }    
			         	 	    }
			         	 	    else{
 									$('.thirdMenu').css('display','none');
			         	 	    }
			                }  
			           }  
			     });
    });

}