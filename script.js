// Agrega un proyecto dinámicamente al hacer clic
$('#agregar-proyecto').on('click', function () {
  $('#proyecto-lista').append(`
    <div class="col-md-4">
      <div class="card mt-3">
        <div class="card-body">
          <h5 class="card-title">Proyecto Nuevo</h5>
          <p class="card-text">Descripción del nuevo proyecto.</p>
        </div>
      </div>
    </div>
  `);
});

// Mostrar mensaje al enviar formulario
$('#formulario-contacto').on('submit', function (e) {
  e.preventDefault();
  alert('Gracias por tu mensaje, te contactaré pronto.');
  this.reset();
});