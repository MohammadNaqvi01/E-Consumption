


 
    
   
function myfunc(id){
    
    take=document.getElementById(id);

        var state=take.innerText
        var id=$('#'+id).parent().attr('id')
    
     if (state=='On'){
    
        

        $.ajax({
            type:"GET",
            url:"/energy",
            data:{
                'appliance':id,
                'state':state
                
            },
            success:function(data){
             alert(data.state) 
             take.className='btn-success'
              
            }
        });

     }
    
if(state=='Off'){

    $.ajax({
        type:"GET",
        url:"/energy",
        data:{
            'appliance':id,
            'state':state
            
        },
        success:function(data){
          alert("Your Electricity Consumption during "+ data.secs+ " secs is "+data.consumption+" kwh")
         take.className='btn-danger'
          
        }
    });


}                               



     }





