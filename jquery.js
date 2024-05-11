
$(function(){


    $('#btn-carro.btn.btn-primary.btn-lg').click(function(){
        alert("Función en desarrollo.");
    })
    

    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {
           var dolar = data.dolar.valor;
           var precio = $('.precioJuego').html(); 
           var precioDolarizado = Math.round(precio / dolar);
            $('.precioJuego').text("$"+ precioDolarizado + " USD" ); 
        }).fail(function() {
    console.log('Error al consumir la API!');
        })
    })


})