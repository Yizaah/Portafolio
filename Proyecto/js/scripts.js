    document.addEventListener('DOMContentLoaded', () => {
  // Modal Cliente
  const modalCliente = document.getElementById('modalCliente');
  const abrirModalCliente = document.getElementById('abrirModalCliente');
  const cerrarModalCliente = document.getElementById('cerrarModalCliente');
  if (abrirModalCliente && modalCliente) {
    abrirModalCliente.onclick = () => modalCliente.style.display = 'flex';
    cerrarModalCliente.onclick = () => modalCliente.style.display = 'none';
    window.onclick = (e) => { if (e.target === modalCliente) modalCliente.style.display = 'none'; };
  }

  // Mostrar campos según tipo de cliente
  const tipoCliente = document.getElementById('tipo_cliente');
  if (tipoCliente) {
    tipoCliente.addEventListener('change', () => {
      document.getElementById('datos_persona').style.display = tipoCliente.value === 'persona' ? 'block' : 'none';
      document.getElementById('datos_empresa').style.display = tipoCliente.value === 'empresa' ? 'block' : 'none';
    });
  }

  // Guardar cliente y mostrar en tabla
  const formCliente = document.getElementById('form_cliente');
  const tablaClientes = document.getElementById('tablaClientes')?.querySelector('tbody');
  if (formCliente && tablaClientes) {
    formCliente.addEventListener('submit', (e) => {
      e.preventDefault();
      let tipo = tipoCliente.value;
      let nombre = tipo === 'persona' ? document.getElementById('nombre').value : document.getElementById('razon_social').value;
      let rut = tipo === 'persona' ? document.getElementById('rut').value : document.getElementById('rut_empresa').value;
      let telefono = document.getElementById('telefono').value;
      let email = document.getElementById('email').value;
      let direccion = document.getElementById('direccion').value;
      let fila = `<tr>
        <td>${tipo}</td>
        <td>${nombre}</td>
        <td>${rut}</td>
        <td>${telefono}</td>
        <td>${email}</td>
        <td>${direccion}</td>
      </tr>`;
      tablaClientes.innerHTML += fila;
      formCliente.reset();
      document.getElementById('datos_persona').style.display = 'none';
      document.getElementById('datos_empresa').style.display = 'none';
      modalCliente.style.display = 'none';
    });
  }

  // Modal Causa (similar, para causas.html)
  const modalCausa = document.getElementById('modalCausa');
  const abrirModalCausa = document.getElementById('abrirModalCausa');
  const cerrarModalCausa = document.getElementById('cerrarModalCausa');
  if (abrirModalCausa && modalCausa) {
    abrirModalCausa.onclick = () => modalCausa.style.display = 'flex';
    cerrarModalCausa.onclick = () => modalCausa.style.display = 'none';
    window.onclick = (e) => { if (e.target === modalCausa) modalCausa.style.display = 'none'; };
  }

  // Mostrar campo RUC solo para Penal
  const tipoExpediente = document.getElementById('tipo_expediente');
  if (tipoExpediente) {
    tipoExpediente.addEventListener('change', () => {
      document.getElementById('campo_ruc').style.display = tipoExpediente.value === 'Penal' ? 'block' : 'none';
    });
  }

  // Guardar causa y mostrar en tabla
  const formCausa = document.getElementById('form_causa');
  const tablaCausas = document.getElementById('tablaCausas')?.querySelector('tbody');
  if (formCausa && tablaCausas) {
    formCausa.addEventListener('submit', (e) => {
      e.preventDefault();
      let rol = document.getElementById('rol').value;
      let cliente = document.getElementById('cliente').options[document.getElementById('cliente').selectedIndex].text;
      let tipo = tipoExpediente.value;
      let ruc = document.getElementById('ruc').value;
      let titulo = document.getElementById('titulo').value;
      let estado = document.getElementById('estado').value;
      let fila = `<tr>
        <td>${rol}</td>
        <td>${cliente}</td>
        <td>${tipo}</td>
        <td>${ruc}</td>
        <td>${titulo}</td>
        <td>${estado}</td>
      </tr>`;
      tablaCausas.innerHTML += fila;
      formCausa.reset();
      document.getElementById('campo_ruc').style.display = 'none';
      modalCausa.style.display = 'none';
    });
  }
});