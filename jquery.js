
$(function(){


    $('#btn-carro.btn.btn-primary.btn-lg').click(function(){
        alert("Función en desarrollo.");
    })
    

    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {
            if ($('.btnConversion').text().trim() == "Convertir a dólares"){
                var dolar = data.dolar.valor;
                var precio = $('.precioJuego').text().substring(1, $('.precioJuego').text().length-4).replaceAll('.', '');
                var precioDolarizado = Math.round(precio / dolar);
                $('.precioJuegoConvertido').text("$"+ precioDolarizado + " USD");
                $('.precioJuego').hide();
                $('.precioJuegoConvertido').show();
                $('.btnConversion').text("Convertir a pesos");
            }
            else if ($('.btnConversion').text().trim() == "Convertir a pesos"){
                $('.precioJuego').show();
                $('.precioJuegoConvertido').hide();
                $('.btnConversion').text("Convertir a dólares"); 
            }
        }).fail(function() {
    console.log('Error al consumir la API!');
        })
    })


    //verificaciones
    $('#enviarRegistro').click(function(){
        var test = $.trim($('.txtRut').val());
       if($.trim($('.txtRut').val())==""){
        alert("Ingrese rut válido")
        $('.txtRut').focus();
       }
       else if($.trim($('.txtNombre').val())==""){
        alert("Ingrese nombre")
        $('.txtNombre').focus();
       }
       else if($.trim($('.txtApellido').val())==""){
        alert("Ingrese apellido")
        $('.txtApellido').focus();
       }
       else if($.trim($('.txtEmail').val())==""){
        alert("Ingrese email válido")
        $('.txtEmail').focus();
       }

    })


})