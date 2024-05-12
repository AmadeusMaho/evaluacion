
$(function(){
    
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

    //carro
    function agregarElemento(imagen, nombre, precio, cantidad, total) {
        var nuevoItem = $('.carrito');
        var imagen = $('.img-producto').text();
        alert(imagen);
        nuevoItem.append('<th scope="row" class="numero-tabla">' + imagen + '</th>');
        nuevoItem.append('<td class="imagen-tabla">' + producto + '</td>');
        nuevoItem.append('<td class="titulo-tabla">' + titulo + '</td>');
        nuevoItem.append('<td class="precio-tabla">' + precio + '</td>');
        $('#tabla-productos tbody').append(nuevoItem);
      }


    //verificaciones
    $('#enviarRegistro').click(function(){
        var rut = $.trim($('.txtRut').val());
       if($.trim($('.txtRut').val())==""){
        alert("Ingrese rut válido")
        $('.txtRut').focus();
       }
       else if(!(/^\d{8}-[\dk]{1}$/.test(rut))){
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