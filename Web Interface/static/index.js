$(document).ready(function() {
    
    $(function() {
        $('#indbtn').click();
    });

    window.setInterval(function(){
        document.getElementById("indbtn").click();}, 8000);

    $('.updateButton').on('click', function() {
        req = $.ajax({
            url : '/index_update',
            type : 'POST',
        });
  
        req.done(function(data) {
  
            $('.live-data').fadeOut(400).fadeIn(400);

            $('#nifty50val').text(data.nifty50[1]);
            $('#nifty50chng').text(data.nifty50[2]+" ("+data.nifty50[3]+"%)");

            $('#niftybankval').text(data.niftybank[1]);
            $('#niftybankchng').text(data.niftybank[2]+" ("+data.niftybank[3]+"%)");

            $('#niftymidval').text(data.niftymid[1]);
            $('#niftymidchng').text(data.niftymid[2]+" ("+data.niftymid[3]+"%)");

            $('#niftyitval').text(data.niftyit[1]);
            $('#niftyitchng').text(data.niftyit[2]+" ("+data.niftyit[3]+"%)");

            $('#niftyfinval').text(data.niftyfin[1]);
            $('#niftyfinchng').text(data.niftyfin[2]+" ("+data.niftyfin[3]+"%)");
        });
      });
  });