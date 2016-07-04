$(function() {

    $("#publishForm").validate({
    
        rules: {
            nombre_mascota: {
                required: true,
                maxlength: 20
            },
            especie: {
                required: true
            },
            raza: {
                required: true
            },
            color: {
                required: true
            },
            sexo: {
                required: true
            },
            fecha_perdido: {
                required: true
            },
            ultimo_lugar: {
                required: true
            },
            mas_informacion: {
                required: true
            }
        },
        
        messages: {
            nombre_mascota: {
                required: "Ingrese Nombre de la Mascota",
                maxlength: "Demasiados caracteres"
            },
            especie: {
                required: "Ingrese la especie de tu mascota (ejem. perro, gato, etc)"
            },
            raza: {
                required: "Ingrese la raza de tu mascota"
            },
            color: {
                required: "Ingrese el color de tu mascota"
            },
            sexo: {
                required: "Seleccione sexo"
            },
            fecha_perdido: {
                required: "Ingrese Fecha cuando se perdio"
            },
            ultimo_lugar: {
                required: "Ingrese ultimo lugar donde fue vista su mascota"
            },
            mas_informacion: {
                required: "Ingrese mas informacion de tu anuncio para facilitar la busqueda a otras personas"
            }
        },
        
        submitHandler: function(form) {
            form.submit();
        }

    });

});