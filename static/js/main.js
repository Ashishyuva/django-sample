
$( document ).ready(function() {
    //var $modal = $('#myModal');
   $(".ajax-button").click(function(e) {
      e.preventDefault();
      var purchase_id = $(this).attr("id").split("item_")[1]
      var url_send= '/shops/payment_model/'+purchase_id +"/"
      $.ajax({ // create an AJAX call...
                data: {item_id:purchase_id },// get the form data
                type: "GET", // GET or POST
                url:  url_send,// the file to call
                success: function(response) { // on 
               // var target = "/shops/payment_model/{{item.id}}";
                  $("#success").html(response)
                      $("#myModal").modal("show"); 
                }
           });
      });
   });

$(document).ready(function() {
      $(".item_edit").submit(function(){
         form_edit_item = $(this).attr("id").split("_")[1]
        // formData = new FormData(this);
      //  data_all = $("#edit_"+ form_edit_item).serialize();
         // formObj = $(this);
         // formURL = formObj.attr("action");
         // formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: "/shops/update_item/",
             data:  $("#edit_"+ form_edit_item).serialize(),
              // mimeType:"multipart/form-data",
              // contentType: false,
              // cache: false,
              // processData:false,
               success: function(response) { 
                $(".btn-warning").click();
                  $("#all_items").html(response)
                   

               }
               // error: function(jqXHR, textStatus, errorThrown)
               // {
               // }         
              });
                 return false;

              // e.preventDefault(); //Prevent Default action.
              // e.unbind();
           });
    
   });