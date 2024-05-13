
$(function(){

    $(document).ready(function() {       $('.spinner-border').hide(); });
    $('.btnConversion').click(function(){
        $('.spinner-border').show();
        $('.precioJuego').hide();
        $.getJSON('https://mindicador.cl/api', function(data) {
            if ($('.btnConversion').text().trim() == "Convertir a dólares"){
                var dolar = data.dolar.valor;
                var precio = $('.precioJuego').text().substring(1, $('.precioJuego').text().length-4).replaceAll('.', '');
                var precioDolarizado = Math.round((precio / dolar)*100) / 100; //dos decimales
                $('.spinner-border').hide();
                $('.precioJuegoConvertido').text("$"+ precioDolarizado + " USD");
                $('.precioJuegoConvertido').show();
                $('.btnConversion').text("Convertir a pesos");
            }
            else if ($('.btnConversion').text().trim() == "Convertir a pesos"){
                $('.spinner-border').hide();
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
        $('spinner-border').hide();
      }

    
    $('.btn-carro').click(function(){
    alert("¡Producto agregado con éxito!");
    //agregarElemento('.data-imagen',1,1,1,1)
    })

    // Vista previa
    $('#enviarSerie').click(function(){
        if (!($('.txtSImg').val() == '')){
            var fileInput = $('.txtSImg')[0];
            var file = fileInput.files[0];
            var url = URL.createObjectURL(file);
            $('.vista-previa').attr('src', url);
        }
    })

    $('.btnVistaPreviaS').click(function(){
        if (!($('.txtSImg').val() == '')){
            var fileInput = $('.txtSImg')[0];
            var file = fileInput.files[0];
            var url = URL.createObjectURL(file);
            $('.vista-previa').attr('src', url);
        }
    })

    $('.btnVistaPreviaJ').click(function(){
        if (!($('.txtJImg').val() == '')){
            var fileInput = $('.txtJImg')[0];
            var file = fileInput.files[0];
            var url = URL.createObjectURL(file);
            $('.vista-previa').attr('src', url);
        }
    })

    $('#enviarJuego').click(function(){
        if (!($('.txtJImg').val() == '')){
            var fileInput = $('.txtJImg')[0];
            var file = fileInput.files[0];
            var url = URL.createObjectURL(file);
            $('.vista-previa').attr('src', url);
        }
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
        $('.selectNac')[0].setCustomValidity('');

        var rut = $.trim($('.txtRut').val());
       if($.trim($('.txtRut').val())==""){
        $('.txtRut')[0].setCustomValidity('Ingrese un RUT válido.')
        $('.txtRut').focus();
       }
       else if(!(/^\d{8}-[\dk]{1}$/.test(rut))){
        $('.txtRut')[0].setCustomValidity('Ingrese un RUT válido.')
        $('.txtRut').focus();
       }
       else if($.trim($('.txtNombre').val())==""){
        $('.txtNombre')[0].setCustomValidity('Ingrese un nombre.');
        $('.txtNombre').focus();
       }
       else if($.trim($('.txtApellido').val())==""){
        $('.txtApellido')[0].setCustomValidity('Ingrese un apellido.');
        $('.txtApellido').focus();
       }
       else if($.trim($('.txtEmail').val())==""){
        $('.txtEmail')[0].setCustomValidity('Ingrese un email valido.');
        $('.txtEmail').focus();
       }
       else if(!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($.trim($('.txtEmail').val())))){
        $('.txtEmail')[0].setCustomValidity('Ingrese un email valido.');
        $('.txtEmail').focus();
       }
       else if($.trim($('.txtTelefono').val())==""){
        $('.txtTelefono')[0].setCustomValidity('Ingrese teléfono válido.');
        $('.txtTelefono').focus();
       }
       else if(!(/^[\+]{1}(569|562)[\d]{8}$/.test($.trim($('.txtTelefono').val())))) {
        $('.txtTelefono')[0].setCustomValidity('Debe empezar con +569/+562, 8 digitos.');
        $('.txtTelefono').focus();
        }
       else if($.trim($('.selectRegion').val())=="Seleccionar Región"){
        $('.selectRegion')[0].setCustomValidity('Seleccione una región.');
        $('.selectRegion').focus();
       }
       else if($.trim($('.selectNac').val())=="Seleccionar"){
        $('.selectNac')[0].setCustomValidity("Seleccione fecha de nacimiento.");
        $('.selectNac').focus();
       }
       else if($.trim($('.selectEd').val())=="Seleccionar"){
        $('.selectEd')[0].setCustomValidity("Seleccione un nivel educacional.");
        $('.selectEd').focus();
       }
    })

    $('.txtRut, .txtNombre, .txtApellido, .txtEmail, .txtTelefono, .selectRegion, .selectEd, .selectNac').on('keyup', function() {
        $(this).get(0).setCustomValidity('');
    });
    
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
        $('.vista-previa').attr('src', 'img/placeholder.png');
    })

    $('#limpiarJuego').click(function(){
        $('.txtJNombre').val('');
        $('.txtJDev').val('');
        $('.txtJDesc').val('');
        $('.txtJImg').val('');
        $('.txtJPrecio').val('');
        $('.txtJStock').val('');
        $('.txtJKeys').val('');
        $('.txtJPlataforma').val('');
        $('.vista-previa').attr('src', 'img/placeholder.png');
    })

    $('#enviarSerie').click(function(){
        $('.txtSTitulo, .txtSDesc, .txtSImg, .txtSKeys, .txtSPrecio, .txtSStock, .txtSCategoria, .txtSFecha').each(function() {
            this.setCustomValidity('');

        });
        if($.trim($('.txtSTitulo').val())==""){
            $('.txtSTitulo')[0].setCustomValidity('Ingrese un título.')
            $('.txtSTitulo').focus();
           }
        else if($.trim($('.txtSDesc').val())==""){
        $('.txtSDesc')[0].setCustomValidity('Ingrese una descripción.')
        $('.txtSDesc').focus();
        }
        else if($.trim($('.txtSImg').val())==""){
            $('.txtSImg')[0].setCustomValidity('Seleccione una imagen.')
            $('.txtSImg').focus();
        }
        else if($.trim($('.txtSKeys').val())==""){
            $('.txtSKeys')[0].setCustomValidity('Seleccione un archivo con claves.')
            $('.txtSKeys').focus();
        }
        else if($.trim($('.txtSPrecio').val())==""){
            $('.txtSPrecio')[0].setCustomValidity('Ingrese precio unitario.')
            $('.txtSPrecio').focus();
        }
        else if($.trim($('.txtSStock').val())==""){
            $('.txtSStock')[0].setCustomValidity('Ingrese cantidad de stock disponible.')
            $('.txtSStock').focus();
        }
        else if($.trim($('.txtSCategoria').val())==""){
            $('.txtSCategoria')[0].setCustomValidity('Seleccione una categoría.')
            $('.txtSCategoria').focus();
        }
        else if($.trim($('.txtSFecha').val())==""){
            $('.txtSFecha')[0].setCustomValidity('Seleccione una fecha de lanzamiento.')
            $('.txtSFecha').focus();
        }
        else{
            alert("Serie agregada con éxito.")
        }
    })

    $('.txtSTitulo, .txtSDesc, .txtSImg, .txtSKeys, .txtSPrecio, .txtSStock, .txtSCategoria, .txtSFecha').on('keyup', function() {
        $(this).get(0).setCustomValidity('');
    });



    $('#enviarJuego').click(function(){
        $('.txtJNombre, .txtJDev, .txtJDesc, .txtJImg, .txtJPrecio, .txtJStock, .txtJKeys, .txtJPlataforma').each(function() {
            this.setCustomValidity('');
        });

        if($.trim($('.txtJNombre').val())==""){
            $('.txtJNombre')[0].setCustomValidity('Ingrese un titulo.');
            $('.txtJNombre').focus();
           }
        else if($.trim($('.txtJNombre').val()).length>=20){
            $('.txtJNombre')[0].setCustomValidity('El título no puede tener más de 20 carácteres');
            $('.txtJNombre').focus();
        }
        else if($.trim($('.txtJDev').val())==""){
            $('.txtJDev')[0].setCustomValidity('Ingrese un desarrollador.');
            $('.txtJDev').focus();
        }
        else if($.trim($('.txtJDesc').val())==""){
            $('.txtJDesc')[0].setCustomValidity('Ingrese una descripción del juego.');
            $('.txtJDesc').focus();
        }
        else if($.trim($('.txtJDesc').val()).length>=400){
            $('.txtJNombre')[0].setCustomValidity('Límite de 400 carácteres.');
            $('.txtJNombre').focus();
        }
        else if($.trim($('.txtJImg').val())==""){
            $('.txtJImg')[0].setCustomValidity('Ingrese una imagen.');
            $('.txtJImg').focus();
        }
        else if($.trim($('.txtJPrecio').val())==""){
            $('.txtJPrecio')[0].setCustomValidity('Ingrese un precio unitario.');
            $('.txtJPrecio').focus();
        }
        else if($.trim($('.txtJStock').val())==""){
            $('.txtJStock')[0].setCustomValidity('Debe ingresar stock disponible.');
            $('.txtJStock').focus();
        }
        else if($.trim($('.txtJKeys').val())==""){
            $('.txtJKeys')[0].setCustomValidity('Debe adjuntar las keys, formato ZIP y RAR.');
            $('.txtJKeys').focus();
            
        }
        else if($.trim($('.txtJPlataforma').val())==""){
            $('.txtJPlataforma')[0].setCustomValidity('Ingrese plataforma.');
            $('.txtJPlataforma').focus();
        }
        else{
            alert("Juego agregado con éxito.")
        }
        
    });
    $('.txtJNombre, .txtJDev, .txtJDesc, .txtJImg, .txtJPrecio, .txtJStock, .txtJKeys, .txtJPlataforma').on('keyup', function() {
        $(this).get(0).setCustomValidity('');
    });
    
});