$(document).ready(function() {
    $("#btn-obtener").click(function() {
        $("#id_tbody").empty();
        // hacemos la solicitud http
        $.get("https://chilealerta.com/api/query/?user=demo&select=ultimos_sismos_chile",
            function(data) {
                // leemos el json
                $.each(data.ultimos_sismos_chile, function(i, item) {
                    var fila = "<tr><td>" + item.source + "</td><td>" + item.local_time +
                        "</td><td>" + item.magnitude +
                        "</td><td>" + item.reference + "</td></tr>"
                    $("#tabla-categorias").append(fila);

                });
            });
    });
});