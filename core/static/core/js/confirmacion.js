function confirmarEliminacion(id) {
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/eliminar-hardware/" + id + "/";
        }
    })
}