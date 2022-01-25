$(document).ready(function() {
    $(function() {
        $('#stkbtn').click();
    });

    $(function() {
        $('#predbtn').click();
    });

    window.setInterval(function(){
        document.getElementById("stkbtn").click();}, 8000);

    $('.updateButton').on('click', function() {
        req = $.ajax({
            url : '/stock_update',
            type : 'POST',
        });
  
        req.done(function(data) {
  
           $('.predication-values').fadeOut(400).fadeIn(400);

            $('#openprice').text(data.openprice);
   
            $('#curprice').text(data.curprice);
   
            $('#dhigh').text(data.dhigh);
   
            $('#dlow').text(data.dlow);
   
            $('#h52').text(data.h52);

            $('#l52').text(data.l52)
   
        });
      });

      window.setInterval(function(){
        document.getElementById("predbtn").click();}, 8350);

    $('.predButton').on('click', function() {
        req = $.ajax({
            url : '/pred_update',
            type : 'POST',
        });
  
        req.done(function(data) {
            $('#prediction').text(data.prediction)
               
        });
      });
  });
