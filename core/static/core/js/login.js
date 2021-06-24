$(document).ready(function() {
    $("#login-form").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 5
            },
            contrasena: {
                required: true,
                minlength: 6
            }
        },
        messages: {
            nombre: {
                minlength: "El nombre debe tener al menos 5 caracteres"
            },
            contrasena: {
                contrasena: "Debe tener al menos 6 caracteres"
            }
        }
    });
});


const form = document.getElementById("login-form");

form.addEventListener("submit", function(event) {
    event.preventDefault();
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();
    if (nombre != "" && contrasena != "") {
        alert("Formulario enviado con éxito");

    } else {
        alert("Por favor rellene todos los campos.");
    }
})