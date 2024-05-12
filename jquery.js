
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
        $('.txtRut')[0].setCustomValidity('');
        $('.txtNombre')[0].setCustomValidity('');
        $('.txtApellido')[0].setCustomValidity('');
        $('.txtEmail')[0].setCustomValidity('');
        $('.txtTelefono')[0].setCustomValidity('');
        $('.selectRegion')[0].setCustomValidity('');
        $('.selectEd')[0].setCustomValidity('');

        var rut = $.trim($('.txtRut').val());
       if($.trim($('.txtRut').val())==""){
        $('.txtRut')[0].setCustomValidity('Ingrese un RUT válido')
        $('.txtRut').focus();
       }
       else if(!(/^\d{8}-[\dk]{1}$/.test(rut))){
        $('.txtRut')[0].setCustomValidity('Ingrese un RUT válido')
        $('.txtRut').focus();
       }
       else if($.trim($('.txtNombre').val())==""){
        $('.txtNombre')[0].setCustomValidity('Ingrese un nombre');
        $('.txtNombre').focus();
       }
       else if($.trim($('.txtApellido').val())==""){
        $('.txtApellido')[0].setCustomValidity('Ingrese un apellido');
        $('.txtApellido').focus();
       }
       else if($.trim($('.txtEmail').val())==""){
        $('.txtEmail')[0].setCustomValidity('Ingrese un email valido');
        $('.txtEmail').focus();
       }
       else if(!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($.trim($('.txtEmail').val())))){
        $('.txtEmail')[0].setCustomValidity('Ingrese un email valido');
        $('.txtEmail').focus();
       }
       else if($.trim($('.txtTelefono').val())==""){
        $('.txtTelefono')[0].setCustomValidity('Ingrese teléfono válido');
        $('.txtTelefono').focus();
       }
       else if(!(/^[\+]?[\d]+([\s]?[\d]+){4,14}$/.test($.trim($('.txtTelefono').val())))) {
        $('.txtTelefono')[0].setCustomValidity('Ingrese teléfono válido');
        $('.txtTelefono').focus();
        }
       else if($.trim($('.selectRegion').val())=="Seleccionar Región"){
        $('.selectRegion')[0].setCustomValidity('Seleccione una región');
        $('.selectRegion').focus();
       }
       else if($.trim($('.selectEd').val())=="Seleccionar"){
        $('.selectEd')[0].setCustomValidity("Seleccione un nivel educacional");
        $('.selectEd').focus();
       }
    })


})