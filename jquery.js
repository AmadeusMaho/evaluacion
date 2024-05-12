
$(function(){


    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {
            if ($('.btnConversion').text().trim() == "Convertir a dólares"){
                var dolar = data.dolar.valor;
                var precio = $('.precioJuego').text().substring(1, $('.precioJuego').text().length-4).replaceAll('.', '');
                var precioDolarizado = Math.round((precio / dolar)*100) / 100; //dos decimales
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

    //imágenes API
    Fancybox.bind('[data-fancybox="galeria1"]', {
      });
    Fancybox.bind('[data-fancybox="galeria2"]', { 
      });
    Fancybox.bind('[data-fancybox="galeria3"]', {
      });
    Fancybox.bind('[data-fancybox="galeria4"]', { 
      });
    Fancybox.bind('[data-fancybox="galeria5"]', {
      });
    Fancybox.bind('[data-fancybox="galeria6"]', { 
      });
    Fancybox.bind('[data-fancybox="galeria7"]', {
      });


    //carro
    function agregarElemento(imagen, nombre, precio, cantidad, total) {
        var nuevoItem = $('.carrito');
        var imagen = $('.data-precio').text();
        nuevoItem.append('<th scope="row" class="numero-tabla">' + imagen + '</th>');
        $('#tabla-productos tbody').append(nuevoItem);
      }

      $('.btn-carro').click(function(){
        alert("¡Producto agregado con éxito!");
        agregarElemento('.data-imagen',1,1,1,1)
      })

      $('.enviarSerie').click(function(){
        var fileInput = $('.txtSImg')[0];
        var file = fileInput.files[0];
        var url = URL.createObjectURL(file);
        $('.vista-previa').attr('src', url);
      })

      $('.enviarJuego').click(function(){
        var fileInput = $('.txtJImg')[0];
        var file = fileInput.files[0];
        var url = URL.createObjectURL(file);
        $('.vista-previa').attr('src', url);
      })

    //verificaciones 
    //    nuevoItem.append('<td class="imagen-tabla">' + producto + '</td>');
    //    nuevoItem.append('<td class="titulo-tabla">' + titulo + '</td>');
    //    nuevoItem.append('<td class="precio-tabla">' + precio + '</td>');


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
       else if(!(/^[\+]{1}(569|562)[\d]{8}$/.test($.trim($('.txtTelefono').val())))) {
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

    $('#limpiarRegistro').click(function(){
        $('.txtRut').val('');
        $('.txtNombre').val('');
        $('.txtApellido').val('');
        $('.txtEmail').val('');
        $('.txtTelefono').val('');
        $('.selectRegion').val('');
        $('.selectEd').val('');
        $('.selectNac').val('');
    })

    $('#limpiarSerie').click(function(){
        $('.txtSTitulo').val('');
        $('.txtSDesc').val('');
        $('.txtSImg').val('');
        $('.txtSKeys').val('');
        $('.txtSCategoria').val('');
        $('.txtSFecha').val('');
    })

    $('#enviarSerie').click(function(){
        $('.txtSTitulo')[0].setCustomValidity('');
        $('.txtSDesc')[0].setCustomValidity('');
        $('.txtSImg')[0].setCustomValidity('');
        $('.txtSKeys')[0].setCustomValidity('');
        $('.txtSCategoria')[0].setCustomValidity('');
        $('.txtSFecha')[0].setCustomValidity('');
    }) //en progreso
})