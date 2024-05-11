$(function(){

    $('#btn-carro.btn.btn-primary.btn-lg').click(function(){
        alert("Función en desarrollo.");
    })
    

    $('.btnConversion').click(function(){
        $.getJSON('https://mindicador.cl/api', function(data) {
           var dolar = data.dolar.valor;
           var precio = $('.precioJuego').val(); //No agarra el valor del texto, queda en blanco. Apenas lo reciba y le podamos asignar el valor de precioDolarizado 
                                                // debería funcionar (en teoría)
           alert(precio);
           alert("dolar actual: " + dolar);
           var precioDolarizado = dolar * precio;
            $('.precioJuego').val(precioDolarizado); 
        }).fail(function() {
    console.log('Error al consumir la API!');
        })
    })


})