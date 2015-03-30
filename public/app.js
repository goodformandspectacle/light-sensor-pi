FC = {	
    initLight: function() {  
        setInterval(function(){ 
          $.getJSON( "light", function( data ) {
            data = parseInt(data);
            data = (data / 2000) * 75;
            $('img').css('width',data+'%');
        }, 100);
      });
  }
}

jQuery(document).ready(function() {
	FC.initLight();
});
