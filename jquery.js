
$(function(){


    $('#btn-carro.btn.btn-primary.btn-lg').click(function(){
        alert("Función en desarrollo.");
    })
    

    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {

        alert("precio: " + precio);
        alert("dolar: " + dolar);
        if($.trim($('.btnConversion').text=="convertir a doláres.")){
            var dolar = data.dolar.valor;
            const precioOriginal = $('.precioJuego').html(); 
            var precioDolarizado = Math.round(precio / dolar);
    
             $('.precioJuego').text(precioDolarizado); 
             $('.btnConversion').text("convertir a pesos.");   
        }
        else if($.trim($('.btnConversion').text=="convertir a pesos.")){
            $('.precioJuego').text(precioOriginal); 
            $('.btnConversion').text("convertir a doláres.");
        }
             

          
        }).fail(function() {
    console.log('Error al consumir la API!');
        })
    })


})