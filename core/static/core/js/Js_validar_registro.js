$(document).ready(function() {
    $("#contact-form").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 5
            },
            apellido: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email: true
            },
            contrasena: {
                required: true,
                minlength: 6
            }
        }
    });
});

const formulario = document.getElementById("contact-form");

formulario.addEventListener("submit", function(event) {
    event.preventDefault();
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    var email = $('#email').val();
    var contrasena = $('#contrasena').val();
    var checkTerms = $('#checkTerms').is(':checked');

    if (nombre != "" && apellido != "" && email != "" && contrasena != "") {
        if (!checkTerms) {
            alert("Acepte la casilla de terminos y condiciones");
        } else {
            alert("Formulario enviado con éxito");
        }
    } else {
        alert("Por favor rellene todos los campos.");
    }

})