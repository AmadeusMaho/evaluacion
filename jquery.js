
$(function(){


    $('#btn-carro.btn.btn-primary.btn-lg').click(function(){
        alert("Función en desarrollo.");
    })
    

    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {
            if ($('.btnConversion').text().trim() == "convertir a doláres."){
                var dolar = data.dolar.valor;
                var precio = $('.precioJuego').text().substring(1, $('.precioJuego').text().length).replaceAll('.', '');
                var precioDolarizado = Math.round(precio / dolar);
                $('.precioJuegoConvertido').text("$"+ precioDolarizado + " USD");
                $('.precioJuego').hide();
                $('.precioJuegoConvertido').show();
                $('.btnConversion').text("convertir a pesos.");
            }
            else if ($('.btnConversion').text().trim() == "convertir a pesos."){
                $('.precioJuego').show();
                $('.precioJuegoConvertido').hide();
                $('.btnConversion').text("convertir a doláres."); 
            }
        }).fail(function() {
    console.log('Error al consumir la API!');
        })
    })


})