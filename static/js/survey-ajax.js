$(document).ready(function(){
     question_no=0   
     
		$("#add_choices_button").click(function(event){

			
			createchoice()

		});
		$("#ff").submit(function(event){
			alert("inside fff")
			
			 $(this).ajaxSubmit(); 
			return false;
		});

       $("#add_question_button").click(function(event)
       {
       		
       
        
          var fd = $('input[name=csrfmiddlewaretoken]').serialize();
       		context_dict={}
       		question_description= $('input[name=question_description]').val()
       		choice_label= $('input[name="choice_label[]"').map(function(){ return this.value }).get()
       		
       		$.ajax({
               url: '/survey/create_question/'+$("#survey_id_value").val()+'/',
        	   type: 'POST',
			   data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() ,question_description,choice_label },
               dataType:'json',
               success: function(data) 
               {
            //noty({text: data, type: 'success'});
            			
            			console.log(data);
            		
            			if(data.success) 
            			{

                        location.reload();
            					
            			}
            			else
            			{


                      if (data.err)
                      {
                        alert(data.err)
                        $("#error-msg").show()
                        $("#msg").html(data.err)
                      }
                      if (data.choice_description)
                      {  
                        alert(data.choice_description);

                      }
                      if (data.question_description)
                      {
                        alert(data.question_description);
                      }
            				
            			}
            			
            			
            			
            		
               },
        	   error:function (xhr, ajaxOptions)
        	   {
               alert("inside error function")
        	   }
    });
    });
      

function createchoice()
{
	
      choice_data ='<div class="form-group"><input type="text" name="choice_label[]"  placeholder="Add Choice Description" class="form-control"></div>';
	  $("#choiceradiobutton_grp").append(choice_data)
}

function validateform()
{

}



});



